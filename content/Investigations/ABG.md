---
title: "ABG"
tags:
  - internalmedicine
  - investigation
  - diagnostics
status: active
---

# 🩸 Arterial Blood Gas (ABG)

การส่งตรวจแก๊สในเลือดแดงเพื่อประเมินภาวะความเป็นกรด-ด่าง ประสิทธิภาพการแลกเปลี่ยนแก๊ส และระดับการระบายอากาศ (Ventilation) ของผู้ป่วย

---

## 📊 Reference Ranges (ค่าปกติในเลือดแดง)

* **pH**: $7.35 - 7.45$ (ต่ำกว่า 7.35 = Acidemia, สูงกว่า 7.45 = Alkalemia)
* **$\text{PaCO}_2$**: $35 - 45$ mmHg (บ่งชี้ Respiratory component)
* **$\text{HCO}_3^-$**: $22 - 26$ mEq/L (บ่งชี้ Metabolic component)
* **$\text{PaO}_2$**: $80 - 100$ mmHg (ระดับออกซิเจนในเลือดแดง)

---

## 🔍 Systematic Interpretation (ขั้นตอนการแปลผล 5 ขั้นตอน)

### ขั้นตอนที่ 1: ดูค่า pH
* **pH < 7.35**: Acidemia (ภาวะเลือดเป็นกรด)
* **pH > 7.45**: Alkalemia (ภาวะเลือดเป็นด่าง)

### ขั้นตอนที่ 2: หาสาเหตุตั้งต้น (Primary Process)
ตรวจคู่ระหว่าง pH กับ $\text{PaCO}_2$ และ $\text{HCO}_3^-$:
* หาก **pH ต่ำ** (Acidosis):
  * $\text{PaCO}_2 > 45$ mmHg $\rightarrow$ **Respiratory Acidosis**
  * $\text{HCO}_3^- < 22$ mEq/L $\rightarrow$ **Metabolic Acidosis**
* หาก **pH สูง** (Alkalosis):
  * $\text{PaCO}_2 < 35$ mmHg $\rightarrow$ **Respiratory Alkalosis**
  * $\text{HCO}_3^- > 26$ mEq/L $\rightarrow$ **Metabolic Alkalosis**

### ขั้นตอนที่ 3: ตรวจสอบการชดเชย (Compensation)
ประเมินว่าร่างกายมีการชดเชยที่เหมาะสมตามสูตรหรือไม่ (หากอยู่นอกช่วงชดเชยที่คำนวณได้ แสดงว่ามีพยาธิสภาพกรด-ด่างแบบผสม - Mixed disorder):

* **Metabolic Acidosis**: สูตรของ **Winter's Formula**
  $$\text{Expected } \text{PaCO}_2 = (1.5 \times \text{HCO}_3^-) + 8 \pm 2$$
  * *หากวัดได้จริงสูงกว่าค่าที่ได้จากสูตร*: มี Respiratory Acidosis ร่วมด้วย
  * *หากวัดได้จริงต่ำกว่าค่าที่ได้จากสูตร*: มี Respiratory Alkalosis ร่วมด้วย
* **Metabolic Alkalosis**:
  $$\text{Expected } \text{PaCO}_2 = (0.7 \times \text{HCO}_3^-) + 21 \pm 2$$
* **Respiratory Acidosis**:
  * *Acute*: $\text{HCO}_3^-$ เพิ่มขึ้น $1$ mEq/L ต่อ $\text{PaCO}_2$ ที่เพิ่มขึ้นทุก ๆ $10$ mmHg
  * *Chronic*: $\text{HCO}_3^-$ เพิ่มขึ้น $3.5$ mEq/L ต่อ $\text{PaCO}_2$ ที่เพิ่มขึ้นทุก ๆ $10$ mmHg
* **Respiratory Alkalosis**:
  * *Acute*: $\text{HCO}_3^-$ ลดลง $2$ mEq/L ต่อ $\text{PaCO}_2$ ที่ลดลงทุก ๆ $10$ mmHg
  * *Chronic*: $\text{HCO}_3^-$ ลดลง $5$ mEq/L ต่อ $\text{PaCO}_2$ ที่ลดลงทุก ๆ $10$ mmHg

### ขั้นตอนที่ 4: คำนวณ Anion Gap (เฉพาะใน Metabolic Acidosis)
$$\text{Anion Gap (AG)} = \text{Na}^+ - (\text{Cl}^- + \text{HCO}_3^-)$$
* **AG > 12** $\rightarrow$ **High Anion Gap Metabolic Acidosis (HAGMA)**
* **AG $\le$ 12** $\rightarrow$ **Normal Anion Gap Metabolic Acidosis (NAGMA)** (มักเกิดจากท้องเสีย - Diarrhea หรือโรคท่อไต Renal Tubular Acidosis - RTA)

### ขั้นตอนที่ 5: คำนวณ Delta Ratio (เฉพาะใน HAGMA)
ใช้ตรวจสอบการมีกรด-ด่างแบบผสมในผู้ป่วย HAGMA:
$$\Delta\text{ Ratio} = \frac{\Delta\text{ Anion Gap}}{\Delta\text{ } \text{HCO}_3^-} = \frac{\text{Anion Gap} - 12}{24 - \text{HCO}_3^-}$$
* **$< 0.4$**: Mixed HAGMA and NAGMA
* **$1.0 - 2.0$**: Pure HAGMA (เช่น DKA, Lactic acidosis)
* **$> 2.0$**: Mixed HAGMA and Metabolic Alkalosis (เช่น ผู้ป่วย DKA ที่มีอาการอาเจียนรุนแรงสูญเสียกรด)

---

## 💡 Clinical Pearls & Red Flags
> [!WARNING]
> **A-a Gradient (Alveolar-arterial Oxygen Gradient)**:
> คำนวณเพื่อจำแนกสาเหตุของภาวะ Hypoxemia (ออกซิเจนในเลือดต่ำ):
> $$\text{P(A-a)O}_2 = \text{P}_{\text{A}}\text{O}_2 - \text{PaO}_2$$
> โดยที่ $\text{P}_{\text{A}}\text{O}_2 = 150 - (\text{PaCO}_2 / 0.8)$ ในอากาศห้องปกติ
> - **A-a Gradient ปกติ ($< 15$ mmHg)**: Hypoxemia เกิดจาก Hypoventilation (เช่น ยาสลบกดหายใจ) หรือ High altitude (ที่สูง)
> - **A-a Gradient กว้าง/สูง ($> 15$ mmHg)**: Hypoxemia เกิดจากพยาธิสภาพในปอดโดยตรง ได้แก่ **V/Q mismatch** (เช่น PE, Asthma), **Shunt** (เช่น Pneumonia, Pulmonary edema) หรือ **Diffusion limitation** (เช่น Interstitial Lung Disease)

---
* [[Investigations/index|Investigations Index]]
