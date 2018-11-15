from sensob import Sensob
from behavior import Behavior
from reflectance_sensors import ReflectanceSensors
#from k import K


class IRSensob(Sensob):
    def __init__(self):
        super(IRSensob, self).__init__(
            sensors=[ReflectanceSensors(auto_calibrate=True)])

    def update(self):
        if super(IRSensob, self).update():
            min_val, min_index = 1, -1
            ir_vals = self.sensor_values[0]
            for i in range(0, len(ir_vals)):
                if 0.0 < ir_vals[i] < min_val:
                    min_val = ir_vals[i]
                    min_index = i
            self.value = min_index

    # I'm considering making two subclasses of IRSensob:
    # LineFollowerSensob and LineLocaterSensob.
    # In that case, no update()-method will be made here,
    # instead they will be individually redefined in subclasses,
    # based on what type of value is most practical to send to Behaviors


'''
if __name__ == '__main__':
    irSens = IRSensob()
    behave = Behavior(None, IRSensob, 1)
    irSens.behaviors[0].active_flag = False
    print(irSens.behaviors[0].active_flag)
    print(irSens.sensor_values)
    irSens.update()
    print(irSens.sensor_values)
'''