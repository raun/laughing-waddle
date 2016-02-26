# __author__ = 'shanshul'

from flask.ext.script import Manager

from ticketting_system import create_app

import sys

manager = Manager(create_app)


@manager.command
def hello():
    print "hello"


if __name__ == "__main__":
    if sys.argv[1] == 'test':
        manager = Manager(create_app(package_name='ticketting_system', config_name='Testing'))

        @manager.command
        def test():
            import nose

            nose.main(argv=['ticketting_system.test', '-s', '-v', '--with-coverage', '--cover-package', 'ticketting_system'])

        manager.run()
    else:
        manager.run()