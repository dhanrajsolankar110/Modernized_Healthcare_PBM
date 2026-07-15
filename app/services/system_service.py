"""
=========================================================
            SYSTEM CONFIGURATION SERVICE
        Modernized Healthcare PBM Portal
=========================================================
"""

from app.models.setting import Setting


class SystemService:

    @staticmethod
    def get(key, default=None):

        setting = Setting.query.filter_by(
            setting_key=key
        ).first()

        if setting:

            return setting.setting_value

        return default

    @staticmethod
    def set(key, value):

        setting = Setting.query.filter_by(
            setting_key=key
        ).first()

        if setting:

            setting.setting_value = str(value)

            from app.extensions import db

            db.session.commit()

            return True

        return False