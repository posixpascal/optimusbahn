-- Create optimus DB
CREATE TABLE IF NOT EXISTS journeys (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    train_id INT NOT NULL,
    station_id INT NOT NULL,
    name VARCHAR(80),
    status VARCHAR(255),
    platform VARCHAR(20),
    is_delayed BOOLEAN DEFAULT FALSE,
    updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
    created_at TIMESTAMP NOT NULL
);
