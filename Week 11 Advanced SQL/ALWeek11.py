import argparse
import sys
import pyodbc
import matplotlib.pyplot as plt



# Function to execute a SQL query 

def execute_cursor(conn, sql_query: str):
    print(f"Executing query: {sql_query}")
    cursor = conn.cursor()
    cursor.execute(sql_query)

    if "SELECT" in sql_query:
        rows = cursor.fetchall()
        headers = [column[0] for column in cursor.description]
        cursor.commit()
        cursor.close()
        return headers, rows
    else:
        cursor.commit()
        cursor.close()
        return None, None



# Main function (takes category_name as an argument)

def main(category_name: str):
    # Connection string to week_11_database 
    conn_str = (
        "DRIVER={PostgreSQL Unicode};"
        "SERVER=localhost;"
        "PORT=5432;"
        "DATABASE=week_11_database;"
        "UID=postgres;"
        "PWD=1GreenLotus!2345;"
    )
    conn = pyodbc.connect(conn_str)

    # SQL query: group by the category_name and summarize mean_ghg_1990_to_2020
    group_by_query = (
    f"SELECT {category_name}, "
    f"AVG(CAST(mean_ghg_1990_to_2020 AS REAL)) "
    f"FROM epa_ghg "
    f"GROUP BY {category_name} "
    f"ORDER BY {category_name};"
    )


    headers, rows = execute_cursor(conn, sql_query=group_by_query)

    
    print(headers)
    for row in rows:
        print(row)

   
    # Create a bar graph using Matplotlib
  
    # x-axis categories (first column from each row)
    categories = [row[0] for row in rows]
    # y-axis values (second column from each row)
    values = [float(row[1]) for row in rows]

    plt.figure()
    plt.bar(categories, values)
    plt.title(f"mean_ghg_1990_to_2020 by {category_name}")
    plt.xlabel(category_name)
    plt.ylabel("mean_ghg_1990_to_2020")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    return



# Argparse function
def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "category_name",
        type=str,
        choices=[
            "econ_sector",
            "econ_source",
            "sector",
            "subsector",
            "category",
            "fuel",
            "subcategory1",
            "subcategory2",
            "subcategory3",
            "subcategory4",
            "state",
            "ghg",
        ],
        help="Category column to group by",
    )

    return parser.parse_args()



# Standard script entry point 

if __name__ == "__main__":
    args = parse_arguments()
    sys.exit(
        main(
            category_name=args.category_name
        )
    )
