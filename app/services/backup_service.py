"""
=========================================================
            DATABASE BACKUP SERVICE
=========================================================
"""

import os
import shutil
from datetime import datetime


class BackupService:

    @staticmethod
    def create_backup():

        project_root = os.getcwd()

        database = os.path.join(

            project_root,

            "instance",

            "healthcare.db"

        )

        backup_folder = os.path.join(

            project_root,

            "backups"

        )

        os.makedirs(

            backup_folder,

            exist_ok=True

        )

        filename = datetime.now().strftime(

            "PBM_Backup_%Y%m%d_%H%M%S.db"

        )

        backup_path = os.path.join(

            backup_folder,

            filename

        )

        shutil.copy2(

            database,

            backup_path

        )

        return backup_path, filename