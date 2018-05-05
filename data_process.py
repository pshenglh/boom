# coding: utf-8
import os
import re

def convert(base_dir):
    dir = base_dir
    files = os.listdir(dir)
    for f in files:
        p = re.compile(r'^\d{8}-\d{2}-R.txt$')
        rst = p.match(f)
        if rst is not None or f.startswith('DAG'):
            source_file = generate_path(f, base_dir)
            LB_file_name = 'LB-' + f
            PT_file_name = 'PT-' + f
            UP_file_name = 'UP-' + f
            LNUP_file_name = 'LNUP-' + f
            LB_file = generate_path(LB_file_name, base_dir)
            PT_file = generate_path(PT_file_name, base_dir)
            UP_file = generate_path(UP_file_name, base_dir)
            LNUP_file = generate_path(LNUP_file_name, base_dir)
            LB_list = []
            PT_list = []
            UP_list = []
            LNUP_list = []

            line_splited = get_datas(source_file)
            dpdt = []
            for d in line_splited:
                dpdt.append(int(d[2]))
            max_dpdt = max(dpdt)
            up_end = False
            for d in line_splited:
                LB_data = d[7] + ',' + d[8] + '\n'
                PT_data = d[0] + ',' + d[1] + '\n'
                UP_data = d[9] + ',' + d[1] + '\n'
                LNUP_data = d[11] + ',' + d[10] + '\n'
                LB_list.append(LB_data)
                PT_list.append(PT_data)
                if not up_end:
                    if int(d[2]) == max_dpdt:
                        up_end = True
                    else:
                        UP_list.append(UP_data)
                        LNUP_list.append(LNUP_data)

            if not os.path.exists(LB_file):
                with open(LB_file, 'w') as f:
                    for d in LB_list:
                        f.write(d)

            if not os.path.exists(PT_file):
                with open(PT_file, 'w') as f:
                    for d in PT_list:
                        f.write(d)

            if not os.path.exists(UP_file):
                with open(UP_file, 'w') as f:
                    for d in UP_list:
                        f.write(d)

            if not os.path.exists(LNUP_file):
                with open(LNUP_file, 'w') as f:
                    for d in LNUP_list:
                        f.write(d)
    print('done')

def handle_source_file(base_dir, file):
    if file.startswith('LB') or file.startswith('PT') or \
        file.startswith('UP') or file.startswith('LNUP') or \
            not file.endswith('.txt'):
        return
    source_file = generate_path(file, base_dir)
    LB_file_name = 'LB-' + file
    PT_file_name = 'PT-' + file
    UP_file_name = 'UP-' + file
    LNUP_file_name = 'LNUP-' + file
    LB_file = generate_path(LB_file_name, base_dir)
    PT_file = generate_path(PT_file_name, base_dir)
    UP_file = generate_path(UP_file_name, base_dir)
    LNUP_file = generate_path(LNUP_file_name, base_dir)
    LB_list = []
    PT_list = []
    UP_list = []
    LNUP_list = []

    line_splited = get_datas(source_file)
    dpdt = []
    for d in line_splited:
        dpdt.append(int(d[2]))
    max_dpdt = max(dpdt)
    up_end = False
    for d in line_splited:
        LB_data = d[7] + ',' + d[8] + '\n'
        PT_data = d[0] + ',' + d[1] + '\n'
        UP_data = d[9] + ',' + d[1] + '\n'
        LNUP_data = d[11] + ',' + d[10] + '\n'
        LB_list.append(LB_data)
        PT_list.append(PT_data)
        if not up_end:
            if int(d[2]) == max_dpdt:
                up_end = True
            else:
                UP_list.append(UP_data)
                LNUP_list.append(LNUP_data)

    if not os.path.exists(LB_file):
        with open(LB_file, 'w') as f:
            for d in LB_list:
                f.write(d)

    if not os.path.exists(PT_file):
        with open(PT_file, 'w') as f:
            for d in PT_list:
                f.write(d)

    if not os.path.exists(UP_file):
        with open(UP_file, 'w') as f:
            for d in UP_list:
                f.write(d)

    if not os.path.exists(LNUP_file):
        with open(LNUP_file, 'w') as f:
            for d in LNUP_list:
                f.write(d)
    return file + '.'*10 + 'done'



def generate_path(f, base_dir):
    return os.path.join(base_dir, f)

def get_datas(source_file):
    with open(source_file, 'r') as source:
        skip_count = 2
        datas = []
        for l in source:
            if skip_count != 0:
                skip_count -= 1
                continue
            if l[0] == '"':
                break
            line_splited = l.split(',')
            datas.append(line_splited)

    return datas

def get_files(begin, base_dir):
    files = os.listdir(base_dir)
    if begin == 'PT':
        p = re.compile(r'PT-.*.txt')
    elif begin == 'LB':
        p = re.compile(r'LB-.*.txt')
    pt_files = []
    for f in files:
        rst = p.match(f)
        if rst is not None:
            pt_files.append(f)
    return pt_files

def get_time_to_10mpa():
    pt_files = get_files('PT')
    for f in pt_files:
        path = os.path.join(BASE_DIR, f)
        first_line = True
        twenty = True
        thirty = True
        fifty = True
        t_p = []
        with open(path) as pf:
            for l in pf:
                datas = l.split(',')
                time = float(datas[0])
                pressure = int(float(datas[1].split('\n')[0]))
                if first_line:
                    t_p.append((time, pressure))
                    first_line = False
                if twenty and pressure == 20:
                    t_p.append((time, pressure))
                    twenty = False
                if thirty and pressure == 30:
                    t_p.append((time, pressure))
                    thirty = False
                if fifty and pressure == 50:
                    t_p.append((time, pressure))
                    fifty = False
            t_p.append((time, float(datas[1].split('\n')[0])))
        print(f, t_p)

def get_LB(work_dir):
    result = []
    l_data = []
    b_data = []
    files = os.listdir(work_dir)
    for f in files:
        lb_f = re.compile(r'^LB-.*')
        is_lbfile = lb_f.search(f)
        if is_lbfile:
            with open(os.path.join(work_dir, f), 'r') as lb_f:
                for l in lb_f:
                    s = l.split(',')
                    b = float(s[0])
                    l = float(s[1].split('\n')[0])
                    l_data.append(l)
                    b_data.append(b)

            l_sum = 0
            i = 0
            for b in b_data:
                if b > 0.1:
                    break
                i = b_data.index(b)
                l_sum += l_data[i]
            l_behind = l_data[i:]
            l_average = l_sum/float(i+1)
            l_max = max(l_behind)
            b_bhind = b_data[i:]
            j = l_behind.index(l_max)
            bm = b_bhind[j]
            lml0 = l_max/l_average
            filename = f
            s = '%s  l0:%.3f, l_max:%.3f, lm/l0:%.3f, bm:%.3f' % (filename, l_average, l_max, lml0, bm)
            result.append(s)
    return result

