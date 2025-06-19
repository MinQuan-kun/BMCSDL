import csv
import re

# Đường dẫn file input và output
input_file = r'D:\Visual Studio Code\HCMUE\BMCSDL\temp.txt'
output_file = r'D:\Visual Studio Code\HCMUE\BMCSDL\SP_InsertApplication.csv'

# Tiêu đề các cột cần xuất
headers = [
    'SubmittedName', 'SubmittedAddress', 'SubmittedGender', 'SubmittedIDNumber', 'SubmittedPhone',
    'SubmittedEmail', 'SubmittedPassportNumber', 'ApplicationDate', 'SubmittedDistrictID',
    'ResidentID', 'PassportID', 'VerificationDate', 'VerificationBy', 'VerificationNotes',
    'DecisionDate', 'DecisionBy', 'DecisionNotes', 'ProcessedDate', 'ProcessedBy', 'ProcessedNotes'
]

with open(input_file, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

    for line in lines:
        # Bỏ prefix, tách bằng dấu phẩy
        data = re.sub(r"EXEC SP_InsertApplication\s+", "", line).strip().rstrip(";")
        # Tách các phần tử, lưu ý loại bỏ 'N' và dấu nháy đơn
        parts = [x.strip() for x in re.split(r",(?=(?:[^']*'[^']*')*[^']*$)", data)]
        parts = [re.sub(r"^N?'(.*?)'$", r"\1", p) if "'" in p else (p if p != 'NULL' else '') for p in parts]
        writer.writerow(parts)

print(f"✅ Đã xuất file CSV tại: {output_file}")