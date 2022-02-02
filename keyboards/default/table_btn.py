from utils.settings_buttons import ListOfButtons

time_table_btn = ListOfButtons(text=['Расписание'],
                               callback=['tabletime'],
                               align=[1]).reply_keyboard
