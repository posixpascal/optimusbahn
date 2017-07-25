
CREATE TABLE IF NOT EXISTS trains (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80),
    type INT,
    departure VARCHAR(5),
    arrival VARCHAR(5),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
    created_at TIMESTAMP NOT NULL
);
