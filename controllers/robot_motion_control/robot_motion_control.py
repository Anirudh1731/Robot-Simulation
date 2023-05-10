"""lineFollowerBot_code controller."""

from controller import Robot

def drive_robot(robot):

    timestep = 32
    max_speed = 6.28

    # Motors
    left_motor = robot.getDevice('motor_left')
    right_motor = robot.getDevice('motor_right')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    # Enable IR sensors
    left_ir = robot.getDevice('ir_left')
    left_ir.enable(timestep)

    right_ir = robot.getDevice('ir_right')
    right_ir.enable(timestep)
    
    uv=robot.getDevice('ultra')
    uv.enable(timestep)

    while robot.step(64) != -1:
        
        #read IR sensors
        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        ultra_val=uv.getValue()

        print("left: {} right: {}".format(left_ir_value, right_ir_value))
        print(ultra_val)
        left_speed = max_speed
        right_speed = max_speed
        
        if(ultra_val<1000):
            print("GO LEFT")
            right_speed=0
            left_speed=-max_speed-4
            

        # if (left_ir_value > right_ir_value)  and (300 <left_ir_value< 400):
            # print('Go left')
            # left_speed = -max_speed
        # elif (right_ir_value > left_ir_value) and (300 <right_ir_value< 400):
            # print('Go right')
            # right_speed = -max_speed+0.5
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == "__main__":
    my_robot = Robot()
    drive_robot(my_robot)
