package main

// Import necessary drivers and modules
import (
	"github.com/uptrace/bun"
	"github.com/uptrace/bun/dialect/pgdialect"
	"github.com/uptrace/bun/driver/pgdriver"
    "os"
   // "context"
    "fmt"
	"database/sql"
    "log"
    _ "github.com/lib/pq"
)




func main() {

    //Collect dsn connection variables from environment
    username := os.Getenv("DB_USERNAME")
    password := os.Getenv("DB_PASSWORD")
    host := os.Getenv("DB_HOST")
    port := os.Getenv("DB_PORT")

    // Compile variables into dsn string
    fmt.Println("Connecting to the database...")
    dsn := fmt.Sprintf(
		"postgresql://%s:%s@%s:%s/research_match",
		username,
		password,
		host,
		port,
	)
    
    //Attempt to connect to postgresql server
    pgdb := sql.OpenDB(pgdriver.NewConnector(pgdriver.WithDSN(dsn)))
    db := bun.NewDB(pgdb, pgdialect.New())

    //Return anything in the database as a test for the connection
    _, err := db.Exec("SELECT *")
    if err != nil {
        log.Fatalf("Failed to connect to the database: %v", err)
    }

    // Connection successful
    fmt.Println("Connected to the database!")

    // Close the database connection when done
    if err := db.Close(); err != nil {
        log.Fatalf("Error closing the database connection: %v", err)
    }



}