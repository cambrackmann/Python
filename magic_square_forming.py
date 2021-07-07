#!/usr/local/bin/python3

def formingMagicSquare(s):
    l_diag_sum = 0
    r_diag_sum = 0
    
    l_col_sum = 0
    m_col_sum = 0
    r_col_sum = 0
    
    t_row_sum = 0
    m_row_sum = 0
    b_row_sum = 0
    
    for i in range(3):  # Sums of each diag/column/row
        # Diagonals
        l_diag_num = s[i][i]
        l_diag_sum += l_diag_num
        
        r_diag_num = s[i][2 - i]
        r_diag_sum += r_diag_num
        
        # Columns
        l_col_num = s[i][0]
        l_col_sum += l_col_num
        
        m_col_num = s[i][1]
        m_col_sum += m_col_num
        
        r_col_num = s[i][2]
        r_col_sum += r_col_num
        
        #  Rows
        t_row_num = s[0][i]
        t_row_sum += t_row_num
        
        m_row_num = s[1][i]
        m_row_sum += m_row_num
        
        b_row_num = s[2][i]
        b_row_sum += b_row_num
    sums = [l_diag_sum, r_diag_sum, l_col_sum, m_col_sum, r_col_sum, t_row_sum, m_row_sum, b_row_sum]
    avg_sum = sum(sums)/(len(sums))
    
    magic_num = 0
    closest = 37
    for i in sums: # Finds magic sum
        r = abs(avg_sum - i)
        
        if r < closest:
            magic_num = i
            closest = r
    
    sum_diffs = []
    for i in range(len(sums)): # Finds sums difference from magic sum
        if sums[i] != magic_num:
            diff = magic_num - sums[i]
            sum_diffs.append(diff)
        if sums[i] == magic_num:
            sum_diffs.append(0)
    print(sum_diffs)
            
    arr = []
    for i in range(len(sum_diffs)):
        if sum_diffs[i] != 0:
            arr.append(i)
    print(arr)
    
    min_conv = 0
    for i in arr:
        if 0 and 2 and 5 in arr and sum_diffs[0] == sum_diffs[2] == sum_diffs[5]:
            min_conv += abs(sum_diffs[0])
        if 0 and 1 and 2 and 3 and 4 and 5 and 6 and 7 and 8 in arr and sum_diffs[0] == sum_diffs[1] == sum_diffs[2] == sum_diffs[3] == sum_diffs[4] == sum_diffs[5] == sum_diffs[6] == sum_diffs[7] == sum_diffs[8]:
            min_conv += abs(sum_diffs[0])
        if '0' and '7' and '4' in arr and sum_diffs[0] == sum_diffs[7] and sum_diffs[7]== sum_diffs[4]:
            min_conv += abs(sum_diffs[0])
        if 1 and 4 and 5 in arr and sum_diffs[1] == sum_diffs[4] == sum_diffs[5]:
            min_conv += abs(sum_diffs[1])
        if 1 and 2 and 7 in arr and sum_diffs[1] == sum_diffs[2] == sum_diffs[7]:
            min_conv += abs(sum_diffs[1])
        if 3 and 5 in arr and sum_diffs[3] == sum_diffs[5]:
            min_conv += abs(sum_diffs[3])
        if 3 and 7 in arr and sum_diffs[3] == sum_diffs[7]:
            min_conv += abs(sum_diffs[3])
        if 6 and 2 in arr and sum_diffs[6] == sum_diffs[2]:
            min_conv += abs(sum_diffs[6])
        if 6 and 4 in arr and sum_diffs[6] == sum_diffs[4]:
            min_conv += abs(sum_diffs[6])    
    print(min_conv)
    return min_conv
        