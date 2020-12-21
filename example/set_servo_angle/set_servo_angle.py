'''
FashionStar Uart舵机 
> 设置舵机角度 <
--------------------------------------------------
- 作者: 阿凯
- Email: xingshunkai@qq.com
- 更新时间: 2020-12-5
--------------------------------------------------
'''
# 添加uservo.py的系统路径
import sys
sys.path.append("../../src")
# 导入依赖
import time
import struct
import serial
from uservo import UartServoManager

# 参数配置
# 角度定义
SERVO_PORT_NAME =  'COM7' # 舵机串口号
SERVO_BAUDRATE = 115200 # 舵机的波特率
SERVO_ID = 0  # 舵机的ID号

# 数据表定义
ADDRESS_VOLTAGE = 1 # 总线电压值的地址

# 初始化串口
uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
					 parity=serial.PARITY_NONE, stopbits=1,\
					 bytesize=8,timeout=0)
# 初始化舵机管理器
uservo = UartServoManager(uart)

print("设置舵机角度为90.0°")
# 设置舵机角度
uservo.set_servo_angle(SERVO_ID, 90.0)
# 等待舵机静止
uservo.wait()

print("设置舵机角度为-90.0°, 周期1000ms")
# 设置舵机角度(指定周期 单位ms)
uservo.set_servo_angle(SERVO_ID, -90.0, interval=1000)
# 等待舵机静止
uservo.wait()

print("设置舵机角度为90.0°, 设置转速为200 °/s")
# 设置舵机角度(指定转速 单位°/s)
# 注: mean_dps是平均角速度的意思 
# dps: degree per second
uservo.set_servo_angle(SERVO_ID, -90.0, mean_dps=200.0)

print("设置舵机角度为-90.0°, 添加功率限制")
# 设置舵机角度(指定功率 单位mW)
uservo.set_servo_angle(SERVO_ID, 90.0, power=400)
# 等待舵机静止
uservo.wait()