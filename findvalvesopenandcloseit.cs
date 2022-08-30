write to the memory area off the PLCs  find valves that are open and close them
        foreach (string valveName in valvesOpen)
        {
            //notify PLC that valve has been closed
            if (valveName.Contains("FV_"))
            {
                string plc = valveName.Split('_')[1];
                uint address = uint.Parse(valveName.Split('_')[2]);
                plcDictionary[plc].writeInt(address, 0);
            }

            //write to the database that the valve has been closed
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                using (SqlCommand command = new SqlCommand("UPDATE ValveState " +
                    "SET open = 0 " +
                    "WHERE name = @name", connection))
                {
                    command.Parameters.AddWithValue("@name", valveName);
                    command.ExecuteNonQuery();
                }
            }
        }
    }