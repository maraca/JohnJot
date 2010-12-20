#!/usr/bin/python
import urllib
import urllib2
import gflags as flags
import sys

FLAGS = flags.FLAGS

flags.DEFINE_string('host', None, 'URI to query')
flags.DEFINE_string('username', None, 'Username to create')
flags.DEFINE_string('email', None, 'Username\'s email.')
flags.DEFINE_string('password', None, 'Username\'s password.')
flags.DEFINE_string('method', 'POST', 'GET or POST. Default set to POST')
flags.DEFINE_bool('basicauth', True, 'BasicAuth : true/false')

class Client(object):
    """Basic client for HTTP request."""

    def __init__(self, host, method):
        self.host = host
        self.method = method
        self.auth = None
        self.opener = None 

    def create_user(self, username, email, password):
        values = {'username': username,
                  'email': email,
                  'password': password}

        data = urllib.urlencode(values)
        response = self.opener.open(self.host, data)
        return response

    def authenticate(self, username, password, realm):
        """Adds basic auth."""
        self.auth = urllib2.HTTPBasicAuthHandler()
        self.auth.add_password(
                realm=realm,
                uri=self.host,
                user=username,
                passwd=password)
        self.opener = urllib2.build_opener(self.auth)


def main(argv):
    try:
        argv = FLAGS(argv)

    except flags.FlagsError, e:
        print '%s\\nUsage: %s ARGS\\n%s' % (e, sys.argv[0], FLAGS)
        sys.exit(1)

    print FLAGS.host
    client = Client(FLAGS.host, FLAGS.method)
    if FLAGS.basicauth:
        username = 'maraca'
        password = 'maraca'
        realm = 'JohnJot'
        client.authenticate(username, password, realm)
        print 'auth done.'

    client.create_user(FLAGS.username,
                       FLAGS.email,
                       FLAGS.password)
    print response
if __name__ == '__main__':
    main(sys.argv)
