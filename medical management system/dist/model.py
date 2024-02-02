from PyQt5 import QtSql, QtCore, QtWidgets

# 初始化数据库
try:
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./medical_management.db')
    db.open()

    print('数据库连接成功')
except Exception as e:
    print (e)
    print("数据库连接失败")


class model(QtSql.QSqlTableModel):
    def __init__(self,main_window, model_name):
        super().__init__()
        self.main_window = main_window
        # 初始化数据模型
        self.setTable(model_name)
        self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.select()


    def commit(self):
        if self.submitAll():
            self.main_window.label_status.setText('提交成功')
        else:
            self.main_window.label_status.setText('提交失败')
        self.select()
    def products_search(self, text):
        if text:
            self.setFilter(f"物品名称 LIKE '%{text}%' OR 物品编号 LIKE '%{text}%'")
        else:
            self.setFilter("")

    def sales_search(self, text):
        if text:
            self.setFilter(f"就诊日期 LIKE '%{text}%' OR 患者姓名 LIKE '%{text}%' OR 联系方式 LIKE '%{text}%' OR 身份证号 LIKE '%{text}%'")
        else:
            self.setFilter("")
    def purchase_search(self, text):
        if text:
            self.setFilter(f"采购日期 LIKE '%{text}%' OR 供应商 LIKE '%{text}%' OR 联系方式 LIKE '%{text}%'")
        else:
            self.setFilter("")


    # 清单部分

    def add(self):
        select_row = self.main_window.tableView_products.currentIndex().row()

        item_id = self.main_window.model_products.index(select_row, 0).data()
        item_name = self.main_window.model_products.index(select_row, 1).data()
        item_price = self.main_window.model_products.index(select_row, 2).data()
        item_unit = self.main_window.model_products.index(select_row, 4).data()

        self.insertRow(0)
        self.setData(self.index(0, 0), item_id)
        self.setData(self.index(0, 1), item_name)
        self.setData(self.index(0, 5), item_unit)
        self.setData(self.index(0, 2), item_price)
        self.setData(self.index(0, 3), 1.0)

    def caltulate(self):
        bill_sum = 0
        try:
            for i in range(self.rowCount()):
                danjia = float(self.data(self.index(i, 2)))
                shuliang = float(self.data(self.index(i, 3)))

                result = danjia * shuliang
                self.setData(self.index(i, 4), result)
                bill_sum += result
        except Exception as e:
            QtWidgets.QMessageBox.about(None, '提示', '单价或数量中需填入数字！')
            print(e)
            return
        self.main_window.lineEdit_amount.setText(str(bill_sum))
        self.main_window.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

    # 提交sell
    def sell_commit(self):
        date = self.main_window.dateTimeEdit.dateTime().toString("yyyy/MM/dd HH:mm")
        name = self.main_window.lineEdit_client_name.text()
        phone = self.main_window.lineEdit_client_phone.text()
        iDnumber = self.main_window.lineEdit_client_id.text()
        age = self.main_window.lineEdit_client_age.text()
        beizhu = self.main_window.textEdit_baizhu.toPlainText()

        chufang = ""
        for i in range(self.rowCount()):
            item_id = self.index(i, 0).data()
            item_name = self.index(i, 1).data()
            item_shuliang = self.index(i, 3).data()
            item_unit = self.index(i, 5).data()
            item = item_name + "*" + str(item_shuliang) + item_unit + " "
            chufang = chufang + item
            # 库存中减少提交的数量
            db.exec(f"UPDATE products SET 库存数量 = 库存数量 - {item_shuliang} WHERE 物品编号 = {item_id}")
            self.main_window.model_products.select()

        biaodan = [date, name, phone, iDnumber, age, chufang, beizhu]
        self.main_window.model_sales.insertRow(0)
        for index, value in enumerate(biaodan):
            self.main_window.model_sales.setData(self.main_window.model_sales.index(0, index), value)

        self.main_window.model_sales.commit()
        self.clear_qingdan()

    def ruku(self):
        supplier_date = self.main_window.dateTimeEdit.dateTime().toString("yyyy/MM/dd HH:mm")
        supplier_name = self.main_window.lineEdit_supplier_name.text()
        supplier_phone = self.main_window.lineEdit_supplier_phone.text()
        beizhu = self.main_window.textEdit_baizhu.toPlainText()

        items = ""
        for i in range(self.rowCount()):
            item_id = self.index(i, 0).data()
            item_name = self.index(i, 1).data()
            item_shuliang = self.index(i, 3).data()
            item_unit = self.index(i, 5).data()
            item = item_name + "*" + str(item_shuliang) + item_unit + " "
            items = items + item
        #     库存中增加提交的数量
            db.exec(f"UPDATE products SET 库存数量 = 库存数量 + {item_shuliang} WHERE 物品编号 = {item_id}")
            self.main_window.model_products.select()

        biaodan = [supplier_date, supplier_name, supplier_phone, items, beizhu]
        self.main_window.model_purchase.insertRow(0)
        for index, value in enumerate(biaodan):
            self.main_window.model_purchase.setData(self.main_window.model_purchase.index(0, index), value)

        self.main_window.model_purchase.commit()
        self.clear_qingdan()


    def clear_qingdan(self):
        self.main_window.model_inventory.select()
        self.main_window.lineEdit_amount.clear()
        self.main_window.lineEdit_client_name.clear()
        self.main_window.lineEdit_client_phone.clear()
        self.main_window.lineEdit_client_age.clear()
        self.main_window.lineEdit_client_id.clear()
        self.main_window.textEdit_baizhu.clear()
        self.main_window.lineEdit_supplier_name.clear()
        self.main_window.lineEdit_supplier_phone.clear()



