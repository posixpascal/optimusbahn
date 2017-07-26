
CREATE TABLE IF NOT EXISTS destinations (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  train_id INT,
  name VARCHAR(80),
  departure VARCHAR(5),
  arrival VARCHAR(5),
  platform VARCHAR(20),
  status VARCHAR(80),
  date TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),

  INDEX destinations_train_index (train_id),
  FOREIGN KEY (train_id)
  REFERENCES trains(id)
    ON DELETE CASCADE
) ENGINE=INNODB;

