from PyQt5 import QtWidgets,uic
import model
class main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        uic.loadUi('./main.ui', self)

        # 初始化products
        self.model_products = model.model(self, 'products')
        self.tableView_products.setModel(self.model_products)
        self.tableView_products.verticalHeader().setVisible(False)
        self.lineEdit_search.textChanged.connect(self.model_products.products_search)

        self.pushButton_inventory_refresh.clicked.connect(lambda :self.model_products.select())
        self.pushButton_inventory_commit.clicked.connect(self.model_products.commit)
        self.pushButton_inventory_insert_row.clicked.connect(lambda :self.model_products.insertRow(0))
        self.pushButton_inventory_row_remove.clicked.connect(lambda :self.model_products.removeRow(self.tableView_products.currentIndex().row()))

        # inventory
        self.model_inventory = model.model(self, 'inventory')
        self.tableView_inventory.setModel(self.model_inventory)
        self.pushButton_add.clicked.connect(self.model_inventory.add)
        self.pushButton_2.clicked.connect(lambda :self.model_inventory.removeRow(self.tableView_inventory.currentIndex().row()))
        self.pushButton_calculate.clicked.connect(self.model_inventory.caltulate)
        self.pushButton_sell.clicked.connect(self.model_inventory.sell_commit)  # 提交sales

        self.pushButton_ruku.clicked.connect(self.model_inventory.ruku) # 提交purchase

        self.pushButton_1.clicked.connect(self.model_inventory.clear_qingdan)


        # sales
        self.model_sales = model.model(self, 'sales')
        self.model_sales.sort(0, 1)
        self.tableView_sales.setModel(self.model_sales)
        self.tableView_sales.verticalHeader().setVisible(False)
        self.tableView_sales.setColumnWidth(5, 500)

        self.pushButton_sales_commit.clicked.connect(self.model_sales.commit)
        self.pushButton_sales_delete.clicked.connect(lambda :self.model_sales.removeRow(self.tableView_sales.currentIndex().row()))
        self.pushButton_sales_refresh.clicked.connect(lambda :self.model_sales.select())
        self.lineEdit_selas_search.textChanged.connect(self.model_sales.sales_search)

        # purchase
        self.model_purchase = model.model(self, 'purchase')
        self.model_purchase.sort(0, 1)
        self.tableView_purchase.setModel(self.model_purchase)
        self.tableView_purchase.verticalHeader().setVisible(False)
        self.tableView_purchase.setColumnWidth(3, 500)

        self.pushButton_pur_refresh.clicked.connect(lambda :self.model_purchase.select())
        self.pushButton_pur_commit.clicked.connect(self.model_purchase.commit)
        self.pushButton_5.clicked.connect(lambda :self.model_purchase.removeRow(self.tableView_purchase.currentIndex().row()))
        self.lineEdit_purchase_search.textChanged.connect(self.model_purchase.purchase_search)

        # # # 设置表格列宽度
        # self.tableView_inventory.setColumnWidth(5, 300)
        # self.tableView_inventory.resizeColumnsToContents()

    def closeEvent(self, event):
        model.db.close()
        event.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_window = main()
    main_window.show()
    app.exec()