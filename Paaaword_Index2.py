import random  # 引入 random 模組，用於隨機打亂和選擇

# 根據使用者選擇生成密碼的索引
def Generate_password_index(E_low, E_big, Num_YN):
    """
    根據使用者輸入，生成一個代表將要使用的字符集（小寫、大寫、數字）的索引。

    參數:
    E_low (str): 'Y' 或 'N'，表示是否包含小寫字母。
    E_big (str): 'Y' 或 'N'，表示是否包含大寫字母。
    Num_YN (str): 'Y' 或 'N'，表示是否包含數字。

    返回值:
    int: 代表字符集組合的密碼索引 (0-7)。
    """
    if E_low == "N" and E_big == "N" and Num_YN == "N": P_index = 0  # 未選擇任何字符，索引為 0
    if E_low == "N" and E_big == "N" and Num_YN == "Y": P_index = 1  # 僅數字
    if E_low == "N" and E_big == "Y" and Num_YN == "N": P_index = 2  # 僅大寫字母
    if E_low == "N" and E_big == "Y" and Num_YN == "Y": P_index = 3  # 大寫字母 + 數字
    if E_low == "Y" and E_big == "N" and Num_YN == "N": P_index = 4  # 僅小寫字母
    if E_low == "Y" and E_big == "N" and Num_YN == "Y": P_index = 5  # 小寫字母 + 數字
    if E_low == "Y" and E_big == "Y" and Num_YN == "N": P_index = 6  # 小寫字母 + 大寫字母
    if E_low == "Y" and E_big == "Y" and Num_YN == "Y": P_index = 7  # 小寫字母 + 大寫字母 + 數字
    return P_index

# 根據選擇的索引生成密碼字符列表
def Generate_password(GP_index, digits_index):
    """
    生成一個包含可用於生成密碼的字符列表。

    參數:
    GP_index (int): 代表字符集組合的索引（由 Generate_password_index 生成）。
    digits_index (int): 密碼的字符數。

    返回值:
    list: 打亂後的字符列表，用於生成密碼。
    """
    # 初始化小寫字母、大寫字母和數字的空列表
    Lower_English = []
    Upper_English = []
    Number_chars = []
    GP_Chars = []  # 儲存生成密碼的字符列表

    # 填充 ASCII 字符到列表
    for i in range(97, 123):  # 小寫字母 (a-z)
        Lower_English.append(chr(i))
    for i in range(65, 91):  # 大寫字母 (A-Z)
        Upper_English.append(chr(i))
    for i in range(48, 58):  # 數字 (0-9)
        Number_chars.append(chr(i))

    # 將所有字符集打亂，增加隨機性
    random.shuffle(Lower_English)
    random.shuffle(Upper_English)
    random.shuffle(Number_chars)

    # 根據 GP_index 選擇合適的字符集組合
    match GP_index:
        case 1: GP_Chars = Number_chars  # 僅數字
        case 2: GP_Chars = Upper_English  # 僅大寫字母
        case 3: GP_Chars = Number_chars + Upper_English  # 數字 + 大寫字母
        case 4: GP_Chars = Lower_English  # 僅小寫字母
        case 5: GP_Chars = Number_chars + Lower_English  # 數字 + 小寫字母
        case 6: GP_Chars = Upper_English + Lower_English  # 大寫字母 + 小寫字母
        case 7: GP_Chars = Upper_English + Lower_English + Number_chars  # 大寫字母 + 小寫字母 + 數字

    # 進一步打亂字符，增加隨機性
    random.shuffle(GP_Chars)
    random.shuffle(GP_Chars)

    # 過濾掉易混淆的字符，如 'O', '0', '1', 'l'
    GP_Chars = list(filter(('O').__ne__, GP_Chars))
    GP_Chars = list(filter(('0').__ne__, GP_Chars))
    GP_Chars = list(filter(('1').__ne__, GP_Chars))
    GP_Chars = list(filter(('l').__ne__, GP_Chars))

    return GP_Chars  # 返回打亂的字符列表

# 根據字符列表生成密碼
def Generate_password_char(password_list, digits_index, groups_index):
    """
    根據字符列表生成並打印多組密碼。

    參數:
    password_list (list): 可供選擇的字符列表。
    digits_index (int): 每組密碼的字符數。
    groups_index (int): 要生成的密碼組數。
    """
    X_index = []  # 用來儲存一組密碼的臨時列表
    for i in range(0, groups_index):  # 迴圈生成多組密碼
        random.shuffle(password_list)  # 隨機打亂字符列表
        X_index.clear()  # 清空臨時列表以生成新密碼
        for y in range(0, digits_index):  # 選取指定數量的字符
            X_index.append(password_list[y])
        string_index = "".join(X_index)  # 將字符組合成字串
        print(string_index)  # 打印生成的密碼

# 主程式塊，負責獲取使用者輸入並生成密碼
if __name__ == "__main__":

    pass_char = []  # 用於儲存密碼生成字符的列表

    # 獲取使用者輸入的密碼偏好
    L_YN = input("是否含有小寫英文 (y/n) :")
    B_YN = input("是否含有大寫英文 (y/n) :")
    num_YN = input("是否含有數字 (y/n) :")
    num_index_1 = int(input("要產生幾位數密碼 : "))  # 每組密碼的字符數
    num_index_2 = int(input("要產生幾組密碼 : "))  # 要生成的密碼組數

    # 將輸入轉換為大寫，以便後續處理
    L_YN = L_YN.upper()
    B_YN = B_YN.upper()
    num_YN = num_YN.upper()

    # 根據使用者偏好生成密碼索引
    GPI_index = Generate_password_index(L_YN, B_YN, num_YN)

    # 如果未選擇任何字符類型則退出程式
    if GPI_index == 0:
        exit()
    else:
        # 生成密碼字符列表
        pass_char = Generate_password(GPI_index, num_index_1)

    # 生成並打印密碼
    Generate_password_char(pass_char, num_index_1, num_index_2)
