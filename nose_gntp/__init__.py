import datetime
from nose.plugins import Plugin
from gntp.config import GrowlNotifier


class Growler(GrowlNotifier):
    def __init__(self):
        GrowlNotifier.__init__(self,
            applicationName='Nose',
            notifications=['Nose', 'Success', 'Failure']
        )

    def message(self, title, message, *args):
        self.notify('Nose', title, message % args)

    def success(self, message, *args):
        self.notify('Success', 'Success', message % args, sticky=True)

    def failed(self, message, *args):
        self.notify('Failure', 'Failed', message % args, sticky=True)


class NoseGrowl(Plugin):
    """Growl notifications for Nose"""

    name = 'growl'

    def begin(self):
        """Send a growl notification when we start our test run"""
        growl = Growler()
        growl.register()
        self.start_time = datetime.datetime.now()
        growl.message('Starting tests....', 'Started at : [%s]', self.start_time.isoformat())

    def finalize(self, result=None):
        """Send a growl message with the results of the test run"""
        growl = Growler()

        self.finish_time = datetime.datetime.now()
        delta = self.finish_time - self.start_time

        endtime_msg = 'Completed in  %s.%s seconds' % (delta.seconds, delta.microseconds)
        if result.wasSuccessful():
            growl.success("%s tests run ok\n%s" % (result.testsRun, endtime_msg))
        else:
            growl.failed("%s tests. %s failed. %s errors\n%s",
                result.testsRun,
                len(result.failures),
                len(result.errors),
                endtime_msg
                )
