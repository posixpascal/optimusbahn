-- Create optimus DB
CREATE TABLE IF NOT EXISTS journeys (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    train_id INT,
    station_id INT NOT NULL,
    status VARCHAR(255),
    platform VARCHAR(20),
    is_delayed BOOLEAN DEFAULT FALSE,
    updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
    created_at TIMESTAMP NOT NULL  DEFAULT NOW(),

    INDEX journeys_train_index (train_id),
    INDEX journeys_station_index (station_id),

    FOREIGN KEY (train_id)
        REFERENCES trains(id)
        ON DELETE CASCADE,

    FOREIGN KEY (station_id)
        REFERENCES stations(id)
        ON DELETE CASCADE
) ENGINE=INNODB;
