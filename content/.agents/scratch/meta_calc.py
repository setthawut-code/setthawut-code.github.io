import math

def run_meta(name, studies):
    print(f"\n=========================================")
    print(f"Meta-analysis for: {name}")
    print(f"=========================================")
    
    y = [] # log RR
    v = [] # within-study variance
    w = [] # fixed-effect weights
    
    for study_name, a, n1, c, n2 in studies:
        # risk ratio
        p1 = a / n1
        p2 = c / n2
        rr = p1 / p2
        
        # log risk ratio
        log_rr = math.log(rr)
        
        # variance
        var = (1.0/a) - (1.0/n1) + (1.0/c) - (1.0/n2)
        
        y.append(log_rr)
        v.append(var)
        w_fe = 1.0 / var
        w.append(w_fe)
        
        # print study-specific RR
        se_log_rr = math.sqrt(var)
        ci_low = math.exp(log_rr - 1.96 * se_log_rr)
        ci_high = math.exp(log_rr + 1.96 * se_log_rr)
        print(f"{study_name:12}: TZP={a}/{n1} ({p1*100:5.2f}%), Plac={c}/{n2} ({p2*100:5.2f}%), RR={rr:5.3f} (95% CI: {ci_low:5.3f}--{ci_high:5.3f})")
    
    # Run subgroup
    # T2DM studies are indices 0, 1, 3
    # Non-T2DM is index 2 (SURMOUNT-1)
    t2dm_indices = [0, 1, 3]
    non_t2dm_indices = [2]
    
    def calculate_subgroup(indices, label):
        sub_y = [y[i] for i in indices]
        sub_v = [v[i] for i in indices]
        sub_w = [w[i] for i in indices]
        
        sum_w = sum(sub_w)
        sum_wy = sum(w_i * y_i for w_i, y_i in zip(sub_w, sub_y))
        y_fe = sum_wy / sum_w
        
        q = sum(w_i * (y_i - y_fe)**2 for w_i, y_i in zip(sub_w, sub_y))
        df = len(indices) - 1
        
        if df > 0 and q > df:
            sum_w2 = sum(w_i**2 for w_i in sub_w)
            tau2 = (q - df) / (sum_w - (sum_w2 / sum_w))
        else:
            tau2 = 0.0
            
        sub_w_re = [1.0 / (v_i + tau2) for v_i in sub_v]
        sum_w_re = sum(sub_w_re)
        y_re = sum(w_i * y_i for w_i, y_i in zip(sub_w_re, sub_y)) / sum_w_re
        se_re = 1.0 / math.sqrt(sum_w_re)
        
        rr_re = math.exp(y_re)
        ci_low = math.exp(y_re - 1.96 * se_re)
        ci_high = math.exp(y_re + 1.96 * se_re)
        
        print(f"Subgroup {label}: RR={rr_re:5.3f} (95% CI: {ci_low:5.3f}--{ci_high:5.3f}), I2={max(0, (q-df)/q*100) if q>0 else 0:5.2f}%")
        return y_re, se_re**2
        
    print("-----------------------------------------")
    t2dm_y, t2dm_v = calculate_subgroup(t2dm_indices, "T2DM")
    non_t2dm_y, non_t2dm_v = calculate_subgroup(non_t2dm_indices, "Non-T2DM")
    
    # Interaction test
    diff = t2dm_y - non_t2dm_y
    se_diff = math.sqrt(t2dm_v + non_t2dm_v)
    z_diff = diff / se_diff
    p_diff = 2.0 * (1.0 - 0.5 * (1.0 + math.erf(abs(z_diff) / math.sqrt(2.0))))
    print(f"Subgroup interaction p-value: {p_diff:5.3f}")

# Nausea
nausea_studies = [
    ("SURPASS-1", 52, 363, 7, 115),
    ("SURPASS-5", 66, 355, 4, 120),
    ("SURMOUNT-1", 567, 1896, 64, 643),
    ("SURMOUNT-2", 131, 623, 20, 315)
]

# Diarrhea
diarrhea_studies = [
    ("SURPASS-1", 47, 363, 9, 115),
    ("SURPASS-5", 48, 355, 10, 120),
    ("SURMOUNT-1", 399, 1896, 45, 643),
    ("SURMOUNT-2", 129, 623, 28, 315)
]

# Vomiting
vomiting_studies = [
    ("SURPASS-1", 13, 363, 2, 115),
    ("SURPASS-5", 22, 355, 2, 120),
    ("SURMOUNT-1", 196, 1896, 13, 643),
    ("SURMOUNT-2", 75, 623, 10, 315)
]

# Constipation
constipation_studies = [
    ("SURPASS-1", 21, 363, 1, 115),
    ("SURPASS-5", 20, 355, 1, 120),
    ("SURMOUNT-1", 291, 1896, 39, 643),
    ("SURMOUNT-2", 53, 623, 13, 315)
]

run_meta("Nausea", nausea_studies)
run_meta("Diarrhea", diarrhea_studies)
run_meta("Vomiting", vomiting_studies)
run_meta("Constipation", constipation_studies)
