import math

def run_meta_full(name, studies):
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")
    
    y = []  # log RR
    v = []  # within-study variance
    w = []  # fixed-effect weights
    
    for study_name, a, n1, c, n2 in studies:
        p1 = a / n1
        p2 = c / n2
        rr = p1 / p2
        log_rr = math.log(rr)
        var = (1.0/a) - (1.0/n1) + (1.0/c) - (1.0/n2)
        
        y.append(log_rr)
        v.append(var)
        w_fe = 1.0 / var
        w.append(w_fe)
        
        se = math.sqrt(var)
        ci_low = math.exp(log_rr - 1.96 * se)
        ci_high = math.exp(log_rr + 1.96 * se)
        
        print(f"  {study_name:12}: events TZP={a}/{n1}, Plac={c}/{n2}")
        print(f"    RR = {rr:.2f} ({ci_low:.2f}--{ci_high:.2f})")
        print(f"    ln(RR) = {log_rr:.4f}, ln(CI_low) = {log_rr - 1.96*se:.4f}, ln(CI_high) = {log_rr + 1.96*se:.4f}")
    
    # FE pooled
    sum_w = sum(w)
    sum_wy = sum(wi * yi for wi, yi in zip(w, y))
    y_fe = sum_wy / sum_w
    
    # Q statistic
    q = sum(wi * (yi - y_fe)**2 for wi, yi in zip(w, y))
    df = len(studies) - 1
    
    # tau^2 (DL)
    sum_w2 = sum(wi**2 for wi in w)
    if q > df:
        tau2 = (q - df) / (sum_w - sum_w2 / sum_w)
    else:
        tau2 = 0.0
    
    # I^2
    i2 = max(0, (q - df) / q * 100) if q > 0 else 0
    
    # RE weights & pooled
    w_re = [1.0 / (vi + tau2) for vi in v]
    sum_w_re = sum(w_re)
    y_re = sum(wi * yi for wi, yi in zip(w_re, y)) / sum_w_re
    se_re = 1.0 / math.sqrt(sum_w_re)
    
    rr_re = math.exp(y_re)
    ci_low_re = math.exp(y_re - 1.96 * se_re)
    ci_high_re = math.exp(y_re + 1.96 * se_re)
    
    z = y_re / se_re
    
    # p-value from chi-sq for Q
    # approximate using normal CDF for z
    p_z = 2.0 * (1.0 - 0.5 * (1.0 + math.erf(abs(z) / math.sqrt(2.0))))
    
    # Weights as percentages
    total_w_re = sum(w_re)
    weight_pcts = [(wi / total_w_re * 100) for wi in w_re]
    
    print(f"\n  --- POOLED ---")
    print(f"  Q = {q:.2f}, df = {df}, I2 = {i2:.1f}%, tau2 = {tau2:.6f}")
    print(f"  Pooled RR (RE) = {rr_re:.2f} ({ci_low_re:.2f}--{ci_high_re:.2f})")
    print(f"  ln(pooled) = {y_re:.4f}, ln(CI_low) = {y_re - 1.96*se_re:.4f}, ln(CI_high) = {y_re + 1.96*se_re:.4f}")
    print(f"  Z = {z:.2f}, p < 0.00001" if p_z < 0.00001 else f"  Z = {z:.2f}, p = {p_z:.5f}")
    print(f"  Weights: {[f'{wp:.1f}%' for wp in weight_pcts]}")
    
    # For funnel plot: SE vs ln(RR) for each study
    print(f"\n  --- FUNNEL PLOT DATA ---")
    for i, (study_name, a, n1, c, n2) in enumerate(studies):
        se_i = math.sqrt(v[i])
        print(f"  {study_name}: ln(RR) = {y[i]:.4f}, SE = {se_i:.4f}")
    
    # Subgroup analysis
    t2dm_idx = [i for i, (name, *_) in enumerate(studies) if 'SURPASS' in name or 'SURMOUNT-2' in name.upper()]
    # Actually: T2DM = SURPASS-1, SURPASS-5, SURMOUNT-2; Non-T2DM = SURMOUNT-1
    t2dm_idx = [0, 1, 3]
    non_t2dm_idx = [2]
    
    def calc_subgroup(indices, label):
        sub_y = [y[i] for i in indices]
        sub_v = [v[i] for i in indices]
        sub_w = [w[i] for i in indices]
        
        sum_w = sum(sub_w)
        sum_wy = sum(wi * yi for wi, yi in zip(sub_w, sub_y))
        y_fe = sum_wy / sum_w
        
        q = sum(wi * (yi - y_fe)**2 for wi, yi in zip(sub_w, sub_y))
        df = len(indices) - 1
        
        if df > 0 and q > df:
            sum_w2 = sum(wi**2 for wi in sub_w)
            tau2 = (q - df) / (sum_w - sum_w2 / sum_w)
        else:
            tau2 = 0.0
            
        w_re = [1.0 / (vi + tau2) for vi in sub_v]
        sum_w_re = sum(w_re)
        y_re = sum(wi * yi for wi, yi in zip(w_re, sub_y)) / sum_w_re
        se_re = 1.0 / math.sqrt(sum_w_re)
        
        rr_re = math.exp(y_re)
        ci_low = math.exp(y_re - 1.96 * se_re)
        ci_high = math.exp(y_re + 1.96 * se_re)
        
        i2 = max(0, (q - df) / q * 100) if q > 0 else 0
        
        print(f"  {label}: RR = {rr_re:.2f} ({ci_low:.2f}--{ci_high:.2f}), I2 = {i2:.1f}%")
        return y_re, se_re**2
    
    print(f"\n  --- SUBGROUPS ---")
    t2dm_y, t2dm_v = calc_subgroup(t2dm_idx, "T2DM")
    non_y, non_v = calc_subgroup(non_t2dm_idx, "Non-T2DM")
    
    diff = t2dm_y - non_y
    se_diff = math.sqrt(t2dm_v + non_v)
    z_diff = diff / se_diff
    p_diff = 2.0 * (1.0 - 0.5 * (1.0 + math.erf(abs(z_diff) / math.sqrt(2.0))))
    print(f"  Interaction p = {p_diff:.3f}")

# === DATA ===
nausea = [
    ("SURPASS-1", 52, 363, 7, 115),
    ("SURPASS-5", 66, 355, 4, 120),
    ("SURMOUNT-1", 567, 1896, 64, 643),
    ("SURMOUNT-2", 131, 623, 20, 315),
]

diarrhea = [
    ("SURPASS-1", 47, 363, 9, 115),
    ("SURPASS-5", 48, 355, 10, 120),
    ("SURMOUNT-1", 399, 1896, 45, 643),
    ("SURMOUNT-2", 129, 623, 28, 315),
]

vomiting = [
    ("SURPASS-1", 13, 363, 2, 115),
    ("SURPASS-5", 22, 355, 2, 120),
    ("SURMOUNT-1", 196, 1896, 13, 643),
    ("SURMOUNT-2", 75, 623, 10, 315),
]

constipation = [
    ("SURPASS-1", 21, 363, 1, 115),
    ("SURPASS-5", 20, 355, 1, 120),
    ("SURMOUNT-1", 291, 1896, 39, 643),
    ("SURMOUNT-2", 53, 623, 13, 315),
]

run_meta_full("NAUSEA", nausea)
run_meta_full("DIARRHEA", diarrhea)
run_meta_full("VOMITING", vomiting)
run_meta_full("CONSTIPATION", constipation)
