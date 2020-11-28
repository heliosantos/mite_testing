from mite.volume_model import Constant, Ramp
from .. import names_datapool

volume_model = Ramp(duration=60, frm=0) + Constant(tps=5, duration=240)


def scenario1():
    return [
        ['mite_scripting:say_hello_journey', names_datapool, volume_model],
    ]
