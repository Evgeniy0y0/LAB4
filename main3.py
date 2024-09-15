## --------------------- Ѻ��� ����� ��-31\1
text = ("Whether you're travelling to the islands or the mountains of Thailand, " ## ��������� ������
         "you're likely to spend at least one night in its capital city on the way."
        " Bangkok might be noisy and polluted but it's also an exciting city with plenty of things to see and do. "
         "Why not make it a longer stay?")
print(text, "\n") ## ���� ������ � �������
print(text.lower(), "\n") ## ���� ������ ����� �������� ����
print("Amount of letter 'a' in text = ", text.count('a') + text.count('A'), "\n") ## ���� ������� ���� "�" � �����
print("Is our text lowercased? ", text.islower(), "\n") ## ���� �� ��������� ������� ����� ����� �������� ����

## --------------------- ������� ����� ��-33\1
print(text.replace(" ", "-"), "\n") ## ������� �� ������ �� ������
print("Is our text alphabetic? ", text.isalpha(), "\n") ## ��������, �� ����� ���������� ���� � ����
print("First occurrence of 'city' is at index: ", text.find("city"), "\n") ## ������ ����� ����� "city"

## --------------------- ³������ ������ ��-35
print(text.title(), "\n") # ���������� ����� ����� ������� ����� � ����� �� ������
print("Text starts with 'Whether'? ", text.startswith("Whether"), "\n") # ��������, �� ���������� ����� � ����� "Whether"
print("Split text into words: ", text.split(), "\n") # ������� ����� �� ������ ���
## --------------------- ������ ��������� ��-33
print(text.count("city"), "\n") #������, ������ ���� ����������� ����� "city"
print("All lowercase:", text.lower(), "\n") #���������� ����� ����� � ����� ������
print("Does it start with 'Whether'?",text.startswith("Whether"), "\n") # ��������, �� ���������� ����� � "Whether"