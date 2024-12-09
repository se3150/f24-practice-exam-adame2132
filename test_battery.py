import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b


def describe_Battery():
    def describe_init():
        def test_initallized_right():
            bat = Battery(100)
            charge = bat.getCharge()
            cap = bat.getCapacity()
            assert charge == 100
            assert cap == 100
            assert bat.external_monitor == None
        def test_intallized_with_monitor():
            m = Mock()
            bat = Battery(100, external_monitor=m)
            charge = bat.getCharge()
            cap = bat.getCapacity()
            assert charge == 100
            assert cap == 100
            assert bat.external_monitor == m

    def describe_getCapacity():
        def test_correct_retrival_capacity(charged_battery):
            bat = charged_battery
            cap = bat.getCapacity()
            assert cap == 100
    def describe_getCharge():
        def test_get_correct_charged_after_init(charged_battery):
            bat = charged_battery
            charge = bat.getCharge()
            assert charge == 100
    def describe_recharge():
        def test_if_battery_gets_charged(partially_charged_battery):
            bat = partially_charged_battery
            bat.recharge(30)
            charge = bat.getCharge()
            assert charge == 100
        def test_dosent_charge_over_capacity(charged_battery):
            bat = charged_battery
            bat.recharge(10)
            charge = bat.getCharge()
            assert charge == 100
        def test_notified_monitor():
            # i have to create a mock object in pass to my external monitor
            mock_monitor = Mock()
            bat = Battery(100, external_monitor=mock_monitor)
            # make sure to read the code carfully since the capacity was fll it skips 
            bat.drain(50)
            bat.recharge(10)
            mock_monitor.notify_recharge.assert_called_once_with(60)
    def describe_drain():
        def test_drains_charge_correctly():
            bat = Battery(100)
            bat.drain(90)
            charge = bat.getCharge()
            assert charge == 10
        def test_drain_doesnt_go_negative():
            bat = Battery(100)
            bat.drain(200)
            charge = bat.getCharge()
            assert charge == 0
        def test_notify_monitor():
            monitor = Mock()
            bat = Battery(100, external_monitor=monitor)
            bat.drain(40)
            monitor.notify_drain.assert_called_once_with(60)

            
