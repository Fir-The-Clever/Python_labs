import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                             QTableWidgetItem, QPushButton, QMessageBox, QScrollArea)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()
        self.setWindowTitle("Расписание")

        self.vbox = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)
        self._create_schedule_tab()
        self._create_subjects_tab()
        self._create_teachers_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="schedule_db",
                                     user="lab7",
                                     password="lab7",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_subjects_tab(self):
        self.subjects_tab = QWidget()
        self.tabs.addTab(self.subjects_tab, "Предметы")

        self.subbox = QVBoxLayout()
        self.subbox1 = QHBoxLayout()
        self.subbox2 = QHBoxLayout()

        self.subbox.addLayout(self.subbox1)
        self.subbox.addLayout(self.subbox2)

        self.subjects_gbox = QGroupBox("Предметы")
        self.subbox1.addWidget(self.subjects_gbox)

        self._create_subjects_table()

        self.update_sub_button = QPushButton("Update")
        self.subbox2.addWidget(self.update_sub_button)
        self.update_sub_button.clicked.connect(self._update_subjects)

        self.subjects_tab.setLayout(self.subbox)

    def _create_teachers_tab(self):
        self.teachers_tab = QWidget()
        self.tabs.addTab(self.teachers_tab, "Преподаватели")

        self.teaturebox = QVBoxLayout()
        self.teaturebox1 = QHBoxLayout()
        self.teaturebox2 = QHBoxLayout()

        self.teaturebox.addLayout(self.teaturebox1)
        self.teaturebox.addLayout(self.teaturebox2)

        self.teachers_gbox = QGroupBox("Преподаватели")
        self.teaturebox1.addWidget(self.teachers_gbox)

        self._create_teachers_table()

        self.update_teachers_button = QPushButton("Обновить")
        self.teaturebox2.addWidget(self.update_teachers_button)
        self.update_teachers_button.clicked.connect(self._update_shedule)

        self.teachers_tab.setLayout(self.teaturebox)

    def _create_schedule_tab(self):
        self.scroll_area = QScrollArea()
        self.tabs.addTab(self.scroll_area, "Расписание")
        self.shedule_tab = QWidget()

        self.svbox = QVBoxLayout()
        self.shbox_mon = QHBoxLayout()
        self.shbox_tue = QHBoxLayout()
        self.shbox_wen = QHBoxLayout()
        self.shbox_tur = QHBoxLayout()
        self.shbox_fri = QHBoxLayout()
        self.shbox_sat = QHBoxLayout()
        self.shbox_button = QHBoxLayout()

        self.svbox.addLayout(self.shbox_mon)
        self.svbox.addLayout(self.shbox_tue)
        self.svbox.addLayout(self.shbox_wen)
        self.svbox.addLayout(self.shbox_tur)
        self.svbox.addLayout(self.shbox_fri)
        self.svbox.addLayout(self.shbox_sat)
        self.svbox.addLayout(self.shbox_button)

        self.monday_gbox = QGroupBox("Понедельник")
        self.shbox_mon.addWidget(self.monday_gbox)
        self._create_table("Понедельник", 'monday')

        self.tuesday_gbox = QGroupBox("Вторник")
        self.shbox_tue.addWidget(self.tuesday_gbox)
        self._create_table("Вторник", 'tuesday')

        self.wensday_gbox = QGroupBox("Среда")
        self.shbox_wen.addWidget(self.wensday_gbox)
        self._create_table("Среда", 'wensday')

        self.tursday_gbox = QGroupBox("Четверг")
        self.shbox_tur.addWidget(self.tursday_gbox)
        self._create_table("Четверг", 'tursday')

        self.friday_gbox = QGroupBox("Пятница")
        self.shbox_fri.addWidget(self.friday_gbox)
        self._create_table("Пятница", 'friday')

        self.saturday_gbox = QGroupBox("Суббота")
        self.shbox_sat.addWidget(self.saturday_gbox)
        self._create_table("Суббота", 'saturday')

        self.update_shedule_button = QPushButton("Update")
        self.shbox_button.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)
        self.scroll_area.setWidget(self.shedule_tab)

    def _create_table(self, day, dayname):
        setattr(self, f'{dayname}_table', QTableWidget())
        getattr(self, f'{dayname}_table').setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        getattr(self, f'{dayname}_table').setColumnCount(5)
        getattr(self, f'{dayname}_table').setHorizontalHeaderLabels(["Предмет", "Начало", "Аудитория", "Преподаватель", ""])

        self._update_table(day, dayname)
        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(getattr(self, f'{dayname}_table'))

        getattr(self, f'{dayname}_gbox').setLayout(self.mvbox)

    def _create_teachers_table(self):
        prefix = "teachers"
        setattr(self, f'{prefix}_table', QTableWidget())
        getattr(self, f'{prefix}_table').setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        getattr(self, f'{prefix}_table').setColumnCount(3)
        getattr(self, f'{prefix}_table').setHorizontalHeaderLabels(["Преподаватель", "Предмет"])

        self._update_teachers_table(prefix)
        self.mvbox_t = QVBoxLayout()
        self.mvbox_t.addWidget(getattr(self, f'{prefix}_table'))

        getattr(self, f'{prefix}_gbox').setLayout(self.mvbox_t)

    def _create_subjects_table(self):
        prefix = "subjects"
        setattr(self, f'{prefix}_table', QTableWidget())
        getattr(self, f'{prefix}_table').setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        getattr(self, f'{prefix}_table').setColumnCount(2)
        getattr(self, f'{prefix}_table').setHorizontalHeaderLabels(["Предмет", ""])

        self._update_subjects_table(prefix)
        self.mvbox_sub = QVBoxLayout()
        self.mvbox_sub.addWidget(getattr(self, f'{prefix}_table'))

        getattr(self, f'{prefix}_gbox').setLayout(self.mvbox_sub)

    def _update_teachers_table(self, prefix):
        self.cursor.execute(f"SELECT * FROM teacher JOIN subject on teacher.sub_id = subject.sub_id")
        records = list(self.cursor.fetchall())
        getattr(self, f'{prefix}_table').setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            teacherDelButton = QPushButton("х")
            getattr(self, f'{prefix}_table').setItem(i, 0, QTableWidgetItem(str(r[1])))
            getattr(self, f'{prefix}_table').setItem(i, 1, QTableWidgetItem(str(r[4])))
            getattr(self, f'{prefix}_table').setCellWidget(i, 2, teacherDelButton)
            teacherDelButton.clicked.connect(lambda ch, num=r[0]: self._drop_teacher_by_id(num, prefix))

        addButton = QPushButton("+")
        getattr(self, f'{prefix}_table').setItem(len(records), 0, QTableWidgetItem(""))
        getattr(self, f'{prefix}_table').setCellWidget(len(records), 2, addButton)
        addButton.clicked.connect(lambda ch, rowNum=len(records): self._add_item_to_teacher_table(rowNum, prefix))

        getattr(self, f'{prefix}_table').resizeRowsToContents()

    def _update_subjects_table(self, prefix):
        self.cursor.execute(f"SELECT * FROM subject")
        records = list(self.cursor.fetchall())
        getattr(self, f'{prefix}_table').setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            subDelButton = QPushButton("х")
            getattr(self, f'{prefix}_table').setItem(i, 0, QTableWidgetItem(str(r[1])))
            getattr(self, f'{prefix}_table').setCellWidget(i, 1, subDelButton)
            subDelButton.clicked.connect(lambda ch, num=r[0]: self._drop_subject_by_id(num, prefix))

        addButton = QPushButton("+")
        getattr(self, f'{prefix}_table').setItem(len(records), 0, QTableWidgetItem(""))
        getattr(self, f'{prefix}_table').setCellWidget(len(records), 1, addButton)
        addButton.clicked.connect(lambda ch, rowNum=len(records): self._add_item_to_subject_table(rowNum, prefix))

        getattr(self, f'{prefix}_table').resizeRowsToContents()

    def _drop_subject_by_id(self, rowId, prefix):
        try:
            self.cursor.execute(f"DELETE FROM timetable WHERE sub_id = '{rowId}'")
            self.cursor.execute(f"DELETE FROM teacher WHERE sub_id = '{rowId}'")
            self.cursor.execute(f"DELETE FROM subject WHERE sub_id = '{rowId}'")
            self.conn.commit()
        except:
            print("Something went wrong")
        self._update_subjects_table(prefix)
        getattr(self, f'{prefix}_table').update()

    def _drop_teacher_by_id(self, rowId, prefix):
        try:
            self.cursor.execute(f"DELETE FROM timetable WHERE t_id = {rowId}")
            self.cursor.execute(f"DELETE FROM teacher WHERE teacher_id = {rowId}")
            self.conn.commit()
        except:
            print("Something went wrong")
        self._update_teachers_table(prefix)
        getattr(self, f'{prefix}_table').update()

    def _add_item_to_subject_table(self, rowNum, prefix):
        new_sub = getattr(self, f'{prefix}_table').item(rowNum, 0).text()
        if new_sub == "":
            return
        self.cursor.execute(f"INSERT INTO subject (title) VALUES ('{new_sub}');")
        self._update_subjects_table(prefix)
        getattr(self, f'{prefix}_table').update()

    def _add_item_to_teacher_table(self, rowNum, prefix):
        new_teacher = getattr(self, f'{prefix}_table').item(rowNum, 0).text()
        sub = getattr(self, f'{prefix}_table').item(rowNum, 1).text()
        if new_teacher == "" or sub == "":
            return

        self.cursor.execute(f"SELECT * FROM subject WHERE title ='{sub}'")
        res = list(self.cursor.fetchall())
        if len(res) == 0:
            self.cursor.execute(f"INSERT INTO subject (title) VALUES ('{sub}');")
            self.cursor.execute(f"SELECT * FROM subject WHERE title ='{sub}'")
        sub_id = list(res[0])[0]

        self.cursor.execute(f"INSERT INTO teacher (full_name, sub_id) VALUES ('{new_teacher}', {sub_id}); ")
        self._update_teachers_table(prefix)
        getattr(self, f'{prefix}_table').update()

    def _update_table(self, day, dayname):
        self.cursor.execute(f"SELECT * FROM timetable JOIN subject on timetable.sub_id = subject.sub_id JOIN teacher "
                            f"on teacher.sub_id = subject.sub_id WHERE day ='{day}'")
        records = list(self.cursor.fetchall())
        getattr(self, f'{dayname}_table').setRowCount(len(records)+1)
        for i, r in enumerate(records):
            r = list(r)
            delButton = QPushButton("х")
            getattr(self, f'{dayname}_table').setItem(i, 0, QTableWidgetItem(str(r[6])))
            getattr(self, f'{dayname}_table').setItem(i, 1, QTableWidgetItem(str(r[4])))
            getattr(self, f'{dayname}_table').setItem(i, 2, QTableWidgetItem(str(r[3])))
            getattr(self, f'{dayname}_table').setItem(i, 3, QTableWidgetItem(str(r[8])))
            getattr(self, f'{dayname}_table').setCellWidget(i, 4, delButton)
            delButton.clicked.connect(lambda ch, num = r[0]: self._drop_item_from_table(num, day, dayname))

        addButton = QPushButton("+")
        getattr(self, f'{dayname}_table').setItem(len(records), 0, QTableWidgetItem(""))
        getattr(self, f'{dayname}_table').setItem(len(records), 1, QTableWidgetItem(""))
        getattr(self, f'{dayname}_table').setItem(len(records), 2, QTableWidgetItem(""))
        getattr(self, f'{dayname}_table').setItem(len(records), 3, QTableWidgetItem(""))
        getattr(self, f'{dayname}_table').setCellWidget(len(records), 4, addButton)
        addButton.clicked.connect(lambda ch, rowNum = len(records): self._add_item_to_table(rowNum, day, dayname))

        getattr(self, f'{dayname}_table').resizeRowsToContents()

    def _add_item_to_table(self, rowNum, day, dayname):
        items = []
        for i in range(4):
            try:
                new_value = getattr(self, f'{dayname}_table').item(rowNum, i).text()
                if new_value == "":
                    return
                items.append(new_value)
            except:
                return

        self.cursor.execute(f"SELECT * FROM subject WHERE title ='{items[0]}'")
        res = list(self.cursor.fetchall())
        if len(res) == 0:
            self.cursor.execute(f"INSERT INTO subject (title) VALUES ('{items[0]}');")
            self.cursor.execute(f"SELECT * FROM subject WHERE title ='{items[0]}'")
        sub_id = list(res[0])[0]

        self.cursor.execute(f"SELECT * FROM teacher WHERE full_name ='{items[3]}'")
        res = list(self.cursor.fetchall())
        if len(res) == 0:
            self.cursor.execute(f"INSERT INTO teacher (full_name, sub_id) VALUES ('{items[3]}', '{sub_id}');")
            self.cursor.execute(f"SELECT * FROM teacher WHERE full_name ='{items[3]}'")
        teacher_id = res[0][0]

        self.cursor.execute(f"INSERT INTO timetable (day, sub_id, room, start) VALUES ('{day}', '{sub_id}', '{items[2]}', '{items[1]}');")
        self._update_table(day, dayname)
        getattr(self, f'{dayname}_table').update()

    def _drop_item_from_table(self, rowId, day, dayname):
        try:
            self.cursor.execute(f"DELETE FROM timetable WHERE t_id = {rowId}")
            self.conn.commit()
        except:
            print("Something went wrong")
        self._update_table(day, dayname)
        getattr(self, f'{dayname}_table').update()

    def _update_shedule(self):
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
        daynames = ["monday", "tuesday", "wensday", "tursday", "friday", "saturday"]
        for i in range(len(days)):
            self._update_table(days[i], daynames[i])
            getattr(self, f'{daynames[i]}_table').update()

    def _update_subjects(self):
        prefix = "subjects"
        self._update_subjects_table(prefix)
        getattr(self, f'{prefix}_table').update()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())

