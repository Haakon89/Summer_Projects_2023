module chessgamehaakon {
    requires javafx.controls;
    requires javafx.fxml;

    opens chessgamehaakon to javafx.fxml;
    exports chessgamehaakon;
}
