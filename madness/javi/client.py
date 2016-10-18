# -*- coding: utf-8 -*-
import falcon
import logging

class Client(object):
    def __init__(self, db_driver=None):
        pass

    def set_get(self, data=None):
        return data

    def exec_get(self, data=None):
        return data

    # def set_post(self, data=None):
    #     field = self.field_parser.parse(type="email", value=data.get("email"))
    #     field = Field(**field)
    #     user = self.user_adapter.build_from_blueprint()
    #     user.credentials.intouch.id = field.value
    #     user.credentials.intouch.pin = data.get("pin")
    #     return user
    #
    # def exec_post(self, user=None):
    #     cache = self.login_adapter.get_pin_cache(key=user.credentials.intouch.id)
    #     if cache.previous == -1:
    #         title = "Invalid Request"
    #         description = dict(msg="You must generate new challenge subpin",
    #                            errCode=1007)
    #         logging.critical("ERR: [%s][%s]" % (title, description))
    #         raise falcon.HTTPBadRequest(title=title, description=description)
    #
    #     if not cache.answer == user.credentials.intouch.pin:
    #         try:
    #             self.login_adapter.decrease_retries(cache=cache)
    #         except NoRetriesLeft:
    #             self.__suspend_account__(doc_id=cache.doc_id)
    #             title = "Suspended Account"
    #             description = dict(msg="Account with email [%s] has been suspended." % cache.key,
    #                                errCode=1005,
    #                                params=dict(support=["support@intouch.com"]))
    #             logging.critical("ERR: [%s][%s]" % (title, description))
    #             raise falcon.HTTPBadRequest(title=title, description=description)
    #
    #         cache.previous = -1
    #         self.login_adapter.flush_cache(cache=cache)
    #
    #         title = "Unauthorized"
    #         description = dict(msg="Incorrect subpin",
    #                            errCode=1008,
    #                            params=dict(total=self.login_adapter.subpin_retries, left=cache.retries))
    #         logging.critical("ERR: [%s][%s]" % (title, description))
    #         raise falcon.HTTPBadRequest(title=title, description=description)
    #
    #     self.login_adapter.delete_cache(cache=cache)
    #
    #     response_body = dict(credentials=dict(user_id=cache.doc_id))
    #     self.activity.set_type(type=ACCEPT)
    #     instrument_data = dict(user_id=cache.doc_id, email=cache.key)
    #     self.activity.set_instrument(**instrument_data)
    #     return response_body
    #
    #
    # def __suspend_account__(self, doc_id=str):
    #     logging.critical("suspending account now....")
    #     self.user_adapter.suspend_account(doc_id=doc_id)
