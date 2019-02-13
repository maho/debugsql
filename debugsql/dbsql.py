'''
Created on 02-02-2011

@author: maho
'''

#pylint: disable=invalid-name,superfluous-parens

import cmd
import logging

from prettytable import PrettyTable

logg = logging.getLogger(__name__)

class Debugsql(object):
    '''
    useful tool to query pretty printed sqls
    '''


    def __init__(self, sess):
        self.sess = sess

    def p(self, sql):
        """ print pretty formatted result of query """
        print(self.g(sql))


    def execute(self,sql,session):
        res = session.execute(sql)
        return res

    def colnames(self,cursor):
        for k in cursor.keys():
            if isinstance(k,int): continue
            yield k

    def g(self, sql, types=False, session=None):
        _s = self.sess
        if session:
            _s = session
        res = self.execute(sql=sql,session=_s)

        header = []

        for k in self.colnames(res):
            header.append(k)

        table = PrettyTable(header)
        for r in res.fetchall():
            if types:
                r = [ "{v}({t})".format(v=x,t=type(x)) for x in r]
            table.add_row(r)

        return table.get_string()


class MyShellCmd(cmd.Cmd):
    def default(self, line):
        MyShellCmd.debugsql_instance.p(line)

    def do_EOF(self, line):
        return True

    @classmethod
    def loop(cls):
        x = cls()
        x.prompt = "SQL>"
        x.cmdloop()



class DebugDjangoSql(Debugsql):
    def execute(self,sql,session=None):
        from django.db import connection
        cur = connection.cursor()
        cur.execute(sql)
        return cur

    def colnames(self,cursor):
        for x in cursor.description:
            yield x[0]

def init(sess,cls=Debugsql):
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins

    MyShellCmd.debugsql_instance = cls(sess)

    builtins.dbsql = MyShellCmd.debugsql_instance
    builtins.dbshell = MyShellCmd.loop

def init_django():
    init(sess = None, cls=DebugDjangoSql)


