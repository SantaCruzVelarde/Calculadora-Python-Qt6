import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton
)
from PyQt6.QtCore import Qt


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setFixedSize(320, 280)
        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        layout.addWidget(QLabel("Número A:"))
        self.entrada_a = QLineEdit()
        self.entrada_a.setPlaceholderText("Ingresa un número")
        layout.addWidget(self.entrada_a)

        layout.addWidget(QLabel("Número B:"))
        self.entrada_b = QLineEdit()
        self.entrada_b.setPlaceholderText("Ingresa un número")
        layout.addWidget(self.entrada_b)

        # BOTONES
        botones_layout = QHBoxLayout()
        for texto, slot in [("+", self._suma), ("-", self._resta),
                             ("*", self._mult), ("/", self._div)]:
            btn = QPushButton(texto)
            btn.clicked.connect(slot)
            botones_layout.addWidget(btn)
        layout.addLayout(botones_layout)

        # RESULTADO
        self.lbl_resultado = QLabel("Resultado: —")
        self.lbl_resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lbl_resultado)

        # LIMPIAR
        btn_clear = QPushButton("Limpiar")
        btn_clear.clicked.connect(self._limpiar)
        layout.addWidget(btn_clear)

    def _obtener_valores(self):
        try:
            a = float(self.entrada_a.text())
            b = float(self.entrada_b.text())
            return a, b
        except ValueError:
            self.lbl_resultado.setText("Error: ingresa números válidos")
            return None

    def _suma(self):
        vals = self._obtener_valores()
        if vals:
            self.lbl_resultado.setText(f"Resultado: {vals[0] + vals[1]}")

    def _resta(self):
        vals = self._obtener_valores()
        if vals:
            self.lbl_resultado.setText(f"Resultado: {vals[0] - vals[1]}")

    def _mult(self):
        vals = self._obtener_valores()
        if vals:
            self.lbl_resultado.setText(f"Resultado: {vals[0] * vals[1]}")

    def _div(self):
        vals = self._obtener_valores()
        if vals:
            a, b = vals
            if b == 0:
                self.lbl_resultado.setText("Error: no se puede dividir entre cero")
            else:
                self.lbl_resultado.setText(f"Resultado: {a / b}")

    def _limpiar(self):
        self.entrada_a.clear()
        self.entrada_b.clear()
        self.lbl_resultado.setText("Resultado: —")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())
