import serial.tools.list_ports
import serial
import time


def list_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"端口: {port.device}, 端口信息: {port.description}")


def open_serial_port(port, baudrate=9600):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"成功连接到 {port} 串口")
        return ser
    except Exception as e:
        print(f"打开串口失败: {e}")
        return None


def read_from_serial(ser):
    if ser:
        while True:
            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting)
                print(f"接收到数据: {data.decode()}")
            time.sleep(0.1)


def write_to_serial(ser, data):
    if ser:
        ser.write(data.encode('utf-8'))
        print(f"发送数据: {data}")


if __name__ == "__main__":
    # list_ports()  # 在运行程序之前，可以先打开这个函数查看自己的端口号
    port = "COM17"  # 这里需要根据实际情况修改端口号
    ser = open_serial_port(port)
    if ser:
        write_to_serial(ser, "你好CUG")
        read_from_serial(ser)


