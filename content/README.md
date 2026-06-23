# 🩺 Med-Year-5 (อายุรศาสตร์ ปี 5)

> **คลังความรู้และดัชนีข้อมูลอายุรศาสตร์** สำหรับการฝึกปฏิบัติงานบนหอผู้ป่วย (Ward), การเตรียมสอบ Long Case / Short Case และสรุปแนวทางการสอบระดับชาติ (NL2) สำหรับนักศึกษาแพทย์ชั้นปีที่ 5

---

## 🗂️ Core Index Navigation (ดัชนีหลัก)

ระบบจัดเก็บโน้ตและดัชนีแบ่งออกเป็น 6 ส่วนหลักตามโครงสร้างทางคลินิก เพื่อการเข้าถึงข้อมูลที่รวดเร็วบนวอร์ด:

| ดัชนีหลัก (Main Index) | คำอธิบาย (Description) | ไฟล์หลัก (Link) |
| :--- | :--- | :--- |
| **01 Symptoms Index** | ดัชนีอาการวิทยาและการวินิจฉัยแยกโรค (Approach by Chief Complaint) | [Symptoms/index.md](file:///c:/Users/MSI%20Bravo15/setthawut-code.github.io/content/Symptoms/index.md) |
| **02 Disease Index** | ดัชนีโรคทางอายุรศาสตร์ แบ่งตามระบบย่อย (Neurology, Cardio, Nephro, etc.) | [Diseases/index.md](file:///c:/Users/MSI%20Bravo15/setthawut-code.github.io/content/Diseases/index.md) |
| **03 Investigation Index** | ดัชนีการส่งตรวจทางห้องปฏิบัติการ ภาพถ่ายรังสี และการตรวจพิเศษต่าง ๆ | [Investigations/index.md](file:///c:/Users/MSI%20Bravo15/setthawut-code.github.io/content/Investigations/index.md) |
| **04 Emergency Index** | ดัชนีและการจัดการภาวะฉุกเฉินวิกฤตทางอายุรกรรม (Emergency Medicine) | [Emergency/index.md](file:///c:/Users/MSI%20Bravo15/setthawut-code.github.io/content/Emergency/index.md) |
| **05 Medication Summary** | สรุปยาสำคัญ ปริมาณการใช้ (Dosage) ข้อบ่งใช้ และ Clinical Pearls | [Medications/index.md](file:///c:/Users/MSI%20Bravo15/setthawut-code.github.io/content/Medications/index.md) |
| **06 Antibiotic Guide** | คู่มือการใช้ยาปฏิชีวนะฉบับสมบูรณ์ (Antibiotic Spectra, Empiric & Pathogen) | [Antibiotics/index.md](file:///c:/Users/MSI%20Bravo15/setthawut-code.github.io/content/Antibiotics/index.md) |

---

## 📂 Directory Structure (โครงสร้างโฟลเดอร์)

```
content/
├── Symptoms/          # รวบรวมแนวทางการ approach ตามอาการเด่น เช่น Chest Pain, Fever, Jaundice
├── Diseases/          # ข้อมูลรายละเอียดโรค แบ่งกลุ่มตามสาขาวิชาหลัก (Hematology, Oncology, GI, etc.)
├── Investigations/    # ดัชนีแล็บ (CBC, Electrolytes, LFT) รังสีวิทยา และหัตถการพิเศษ
├── Emergency/         # แผนผังการกู้ชีพและการจัดการ Sepsis, ACS, Acute Stroke, Shock ฯลฯ
├── Medications/       # สรุปขนาดยาและการปรับเปลี่ยนตามการทำงานของไต/ตับ
└── Antibiotics/       # สรุปกลุ่มยาปฏิชีวนะ Spectrum และยาทางเลือกแรกตามเชื้อก่อโรค
```

---

## 💡 Quick Tips for Ward Round (เคล็ดลับใช้งานบนวอร์ด)
1. **หน้าแรก (Master Index)**: เข้าไปที่ [index.md](file:///c:/Users/MSI%20Bravo15/setthawut-code.github.io/content/index.md) เพื่อดูความเชื่อมโยงของหัวข้อทั้งหมดแบบรวดเร็ว
2. **การค้นหา (Search)**: หากใช้งานผ่าน Quartz บนเว็บ สามารถกดปุ่ม Search (หรือ `Ctrl + K`) ค้นหาชื่อโรค ยา หรือรหัสอาการได้ทันที
3. **การตรวจสอบลิงก์ (Validation)**: หากมีการปรับเปลี่ยนโครงสร้างไฟล์ ให้รันสคริปต์ `verify_links.py` จากคอมมานด์ไลน์เพื่อตรวจสอบความถูกต้องของลิงก์เชื่อมโยงภายในทั้งหมด