class Solution:
    def punishmentNumber(self, n: int) -> int:
        result=[]
        for i in range(1, n+1):
            i_squared = i * i
            int_list= list(str(i_squared))
            int_list=list(map(int, int_list))
            if 1<=i<=9:
                if sum(int_list) == i:
                    result.append(i_squared)
                else:
                    continue
            elif 10<=i<=32:
                sum1 = int_list[0] * 10 + int_list[1] + int_list[2] 
                sum2 = int_list[0] + int_list[1] * 10 + int_list[2] 
                if i == sum1 or i == sum2:
                    result.append(i_squared)
            elif 33<=i<=99:
                sum1 = int_list[0] * 10 + int_list[1] + int_list[2] + int_list[3]
                sum1_1 = int_list[0] * 10 + int_list[1] + int_list[2] * 10 + int_list[3]
                sum2 = int_list[0] + int_list[1] * 10 + int_list[2] + int_list[3]
                sum3 = int_list[0] + int_list[1] + int_list[2] * 10 + int_list[3]
                if i == sum1 or i == sum2 or i == sum3 or i == sum1_1:
                    result.append(i_squared)
            elif 100<=i<=316:
                sum1 = int_list[0] * 100 + int_list[1] * 10 + int_list[2] + int_list[3] + int_list[4]
                sum1_1 = int_list[0] * 100 + int_list[1] * 10 + int_list[2] + int_list[3] * 10 + int_list[4]
                sum2 = int_list[0] + int_list[1] * 100 + int_list[2] * 10 + int_list[3] + int_list[4]
                sum3 = int_list[0] + int_list[1] + int_list[2] * 100 + int_list[3] * 10 + int_list[4]
                sum3_1 = int_list[0]*10 + int_list[1] + int_list[2] * 100 + int_list[3] * 10 + int_list[4]
                if i == sum1 or i == sum2 or i == sum3 or i== sum1_1 or i == sum3_1:
                    result.append(i_squared)
            elif 317<=i<=999:
                sum1 = int_list[0] * 100 + int_list[1] * 10 + int_list[2] + int_list[3] + int_list[4] + int_list[5]
                sum1_1 = int_list[0] * 100 + int_list[1] * 10 + int_list[2] + int_list[3]*100 + int_list[4]*10 + int_list[5]
                sum1_2 = int_list[0] * 100 + int_list[1] * 10 + int_list[2] + int_list[3] + int_list[4]*10 + int_list[5]
                sum1_3 = int_list[0] * 100 + int_list[1] * 10 + int_list[2] + int_list[3]*10 + int_list[4] + int_list[5]
                sum2 = int_list[0] + int_list[1] * 100 + int_list[2] * 10 + int_list[3] + int_list[4] + int_list[5]
                sum2_1 = int_list[0] + int_list[1] * 100 + int_list[2] * 10 + int_list[3] + int_list[4]*10 + int_list[5]
                sum3 = int_list[0] + int_list[1] + int_list[2] * 100 + int_list[3] * 10 + int_list[4] + int_list[5]
                sum3_1 = int_list[0]*10 + int_list[1] + int_list[2] * 100 + int_list[3] * 10 + int_list[4] + int_list[5]
                sum4 = int_list[0] + int_list[1] + int_list[2] + int_list[3] * 100 + int_list[4] * 10 + int_list[5]
                sum4_1 = int_list[0]*100 + int_list[1]*10 + int_list[2] + int_list[3] * 100 + int_list[4] * 10 + int_list[5]
                sum4_2 = int_list[0]+ int_list[1]*10 + int_list[2] + int_list[3] * 100 + int_list[4] * 10 + int_list[5]
                sum4_3 = int_list[0]*10+ int_list[1] + int_list[2] + int_list[3] * 100 + int_list[4] * 10 + int_list[5]
                if i == sum1 or i == sum2 or i == sum3 or i == sum4 or i == sum1_1 or i == sum1_2 or i == sum1_3 or i == sum2_1 or i == sum3_1 or i == sum4_1 or i == sum4_2 or i == sum4_3:
                    result.append(i_squared)
            else:
                result.append(i_squared)
        return sum(result)