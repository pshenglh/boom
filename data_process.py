import os
import json


class Config(object):
    def __init__(self):
        self.config_file = 'config.ini'
        try:
            with open(self.config_file) as f:
                self.data = json.load(f)
            self.B_low = self.data['B_low']
            self.B_high = self.data['B_hight']
        except:
            self.B_low = 0
            self.B_high = 0.1
            self.data = {
                'B_low': self.B_low,
                'B_hight': self.B_high
            }
            self.save()

    def save(self):
        with open(self.config_file, 'w') as f:
            f.write(json.dumps(self.data, indent=4))

config = Config()

class CurveData:

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_content = []
        self.experiment_data_str = []
        self.experiment_data_float = []

    def handle_file(self):
        with open(self.file_path) as fp:
            file_content = []
            for line in fp:
                file_content.append(line.strip('\n').split(','))
        self.file_content = file_content

    def get_data(self):
        if not self.file_content:
            self.handle_file()
        file_content = self.file_content
        exp_data_str = []
        exp_data_float = []
        for c in file_content[2:]:
            try:
                data_line = [float(d) for d in c]
                exp_data_str.append(c)
                exp_data_float.append(data_line)
            except Exception as e:
                break
        self.experiment_data_str = exp_data_str
        self.experiment_data_float = exp_data_float
        return exp_data_str, exp_data_float

    def get_curve_data(self, raw_data, *data_index):
        data_list = []
        for i in data_index:
            data_list.append([d[i] for d in raw_data])
        return data_list

    def generate_file(self, file_path, raw_data, *data_index):
        curve_data = self.get_curve_data(raw_data, *data_index)
        data_one, data_two, *other = curve_data
        with open(file_path, 'w') as fp:
            for i, j in zip(data_one, data_two):
                fp.write(i)
                fp.write(',')
                fp.write(j)
                fp.write('\n')

    def LB_data_curve(self, dist_path, file_name):
        new_name = 'LB_' + file_name
        file_path = os.path.join(dist_path, new_name)
        self.generate_file(file_path, self.experiment_data_str, 7, 8)

    def PT_data_curve(self, dist_path, file_name):
        new_name = 'PT_' + file_name
        file_path = os.path.join(dist_path, new_name)
        self.generate_file(file_path, self.experiment_data_str, 0, 1)

    def UP_data_curve(self, dist_path, file_name):
        new_name = 'UP_' + file_name
        file_path = os.path.join(dist_path, new_name)
        self.generate_file(file_path, self.experiment_data_str, 9, 1)

    def LnUP_data_curve(self, dist_path, file_name):
        new_name = 'LnUP_' + file_name
        file_path = os.path.join(dist_path, new_name)
        dPdt = self.get_curve_data(self.experiment_data_float, 2)
        LnU_float = self.get_curve_data(self.experiment_data_float, 11)
        max_index = dPdt[0].index(max(dPdt[0]))
        LnU, LnP = self.get_curve_data(self.experiment_data_str, 11, 10)
        for i, lnu in enumerate(LnU_float[0]):
            if lnu > 0:
                break
        LnU = LnU[i:max_index+1]
        LnP = LnP[i:max_index+1]
        LnUP_list = list(zip(LnU, LnP))
        self.generate_file(file_path, LnUP_list, 0, 1)

    def all_curve_files(self, dist_path, file_name):
        self.LB_data_curve(dist_path, file_name)
        self.PT_data_curve(dist_path, file_name)
        self.UP_data_curve(dist_path, file_name)
        self.LnUP_data_curve(dist_path, file_name)


class DataProcess:

    def __init__(self, file_path):
        self.curve_data = CurveData(file_path)
        self.curve_data.get_data()

    def LB_data(self):
        B, L = self.curve_data.get_curve_data(self.curve_data.experiment_data_float, 7, 8)
        B_initial = [b for b in B if (b > config.B_low and b < config.B_high)]
        L_initial = L[:len(B_initial)]
        L_init_avg = sum(L_initial) / len(L_initial)
        B_behind = B[len(B_initial):]
        L_behind = L[len(B_initial):]
        L_max = max(L_behind)
        max_index = L_behind.index(L_max)
        B_max = B_behind[max_index]
        processing_combusion_value = L_max / L_init_avg
        return L_init_avg, L_max, B_max, processing_combusion_value



if __name__ == '__main__':
    file_path = 'C:\\Users\pshen\OneDrive\projects\experiment_data_process\data\\20170502-24-R.txt'
    dp = CurveData(file_path)
    dp.get_data()
    dp.LnUP_data_curve('./', os.path.basename(file_path))


