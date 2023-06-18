import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel 
import time

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许访问的源
    allow_credentials=True,  # 支持 cookie
    allow_methods=["*"],  # 允许使用的请求方法
    allow_headers=["*"]  # 允许携带的 Headers
)

'''
triangle part
'''
@app.post('/api/triangle/test')
def triangle_test(info:dict[str, list]):
    res_data = {
        'test_result':[]
    }

    for test_item in info['triangle_test_list']:
       current_time = time.ctime()
       actual = traingle_solve(test_item['A'], test_item['B'], test_item['C'])
       res_data['test_result'].append({'actual':actual, 'info':test_item['expectation'], 'test_time':current_time})
    
    return res_data

def traingle_solve(A:int, B:int, C:int):
    if A < 0:
        return "a can't < 0"
    elif A == 0:
        return "a can't be 0"
    elif A >= 800:
        return "a is not in the range of value"

    if B < 0:
        return "b can't < 0"
    elif B == 0:
        return "b can't be 0"
    elif B >= 800:
        return "b is not in the range of value"
    
    if C < 0:
        return "c can't < 0"
    elif C == 0:
        return "c can't be 0"
    elif C >= 800:
        return "c is not in the range of value"
    
    if A + B <= C or A + C <= B or B + C <= A:
        return "Not triangle"
    
    if A == B and B == C:
        return "Equilateral triangle"
    
    if A == B or A == C or B == C:
        return "Isosceles triangle"
    
    return "Normal triangle"

'''
calendar part
'''
@app.post('/api/calendar/test')
def calendar_test(info:dict[str, list]):
    res_data = {
        'test_result':[]
    }

    for test_item in info['calendar_test_list']:
       current_time = time.ctime()
       actual = calendar_solve(test_item['year'], test_item['month'], test_item['day'])
       res_data['test_result'].append({'actual':actual, 'info':test_item['expectation'], 'test_time':current_time})
    
    return res_data

def check_year(year):
    return year >= 2000 and year <= 2100

def check_month(month):
    return month >= 1 and month <= 12

def check_day(day):
    return day >= 1 and day <= 31

def check_is_leap_year(year):
    return 1 - (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def get_total_day_by_month(month, is_leap_year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif is_leap_year:
        return 29
    else:
        return 28

def check(year, month, day):
    if check_year(year) == False:
        return "Year Exceed"
    if check_month(month) == False:
        return "Month Exceed"
    if check_day(day) == False:
        return "Day Exceed"
    total_day = get_total_day_by_month(month, check_is_leap_year(year))
    if day > total_day:
        return "day is out of range for month"
    return "OK"

def calendar_solve(year:int, month:int, day:int):
    res_str = check(year, month, day)
    if res_str == "OK":
        total_day = get_total_day_by_month(month, check_is_leap_year(year))
        if day == total_day:
            day = 1
            month += 1
            if month == 13:
                month = 1
                year += 1
        else:
            day += 1
        return f'{year}-{month}-{day}'
    return res_str

'''
computer sale system part
'''
@app.post('/api/sales/test')
def sales_test(info:dict[str, list]):
    res_data = {
        'test_result':[]
    }

    for test_item in info['sales_test_list']:
       current_time = time.ctime()
       test_result = sales_solve(int(test_item['M']), int(test_item['I']), int(test_item['P']))
       res_data['test_result'].append({'amount':test_result['amount'], 'actual':test_result['amount'], 'earn':test_result['earn'], 'test_time':current_time})
    
    return res_data

def sales_solve(M:int, I:int, P:int):
    if M == -1:
        return {"amount":"系统自动计算本月销售总额", "earn":"系统自动计算本月销售总额"}

    if M <= 0 or I <= 0 or P <= 0:
        return {"amount":"错误，销售员至少销售一台完整的机器", "earn":"错误，销售员至少销售一台完整的机器"}
    if M > 70:
        return {"amount":"错误，主机数量超出限制", "earn":"错误，主机数量超出限制"}
    if I > 80:
        return {"amount":"错误，显示器数量超出限制", "earn":"错误，显示器数量超出限制"}
    if P > 90:
        return {"amount":"错误，外设数量超出限制", "earn":"错误，外设数量超出限制"}
    
    amount = 25 * M + 30 * I + 45 * P
    earn = 0
    if amount <= 1000:
        earn = amount * 0.1
    elif amount <= 1800:
        earn = amount * 0.15
    else:
        earn = amount * 0.2
    
    return {"amount":str(amount), "earn":str(earn)}

'''
cash system part
'''
@app.post('/api/cash/test')
def cash_test(info:dict[str, list]):
    res_data = {
        'test_result':[]
    }

    for test_item in info['cash_test_list']:
       current_time = time.ctime()
       actual = cash_solve(test_item['X'], test_item['Y'])
       res_data['test_result'].append({'actual':actual, 'info':actual, 'test_time':current_time})
    
    return res_data

def cash_solve(X:int, Y:int):
    if X < 0:
        return "The number of minutes of calls cannot be less than 0"
    if Y < 0:
        return "The times of not paying ontime cannot be less than 0"
    if X > 44640:
        return "Call minutes exceed maximum time limit"
    if Y > 11:
        return "The times of not paying ontime cannot be greater than 11"
    if X <= 60:
        if Y <= 1:
            return 25 + X * 0.15 * 0.99
        else:
            return 25 + X * 0.15
    elif X <= 120:
        if Y <= 2:
            return 25 + X * 0.15 * 0.985
        else:
            return 25 + X * 0.15
    elif X <= 180:
        if Y <= 3:
            return 25 + X * 0.15 * 0.98
        else:
            return 25 + X * 0.15
    elif X <= 300:
        if Y <= 3:
            return 25 + X * 0.15 * 0.975
        else:
            return 25 + X * 0.15
    else:
        if Y <= 6:
            return 25 + X * 0.15 * 0.97
        else:
            return 25 + X * 0.15
    return 0


if __name__ == "__main__":
    uvicorn.run(app=app, host='127.0.0.1', port=5000, log_level="debug")