        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            //button to read the data from the PLCs.

            if (m_client.Connected == true)
            {
                if (m_client.ReadDeviceBlock("M30", 1, DataType.DataTypeString) != null)
                {
                    textBox1.Text = (string)m_client.ReadDeviceBlock("M30", 1, DataType.DataTypeString);
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //button to start a client
            if (m_client.Connected == false)
            {
                m_client.Connect();
                Thread.Sleep(250);
                if (m_client.Connected == true)
                {
                    button2.Text = "Disconnect";
                    button2.BackColor = Color.Red;
                }
            }
            else if (m_client.Connected == true)
            {
                m_client.Disconnect();
                Thread.Sleep(250);
                if (m_client.Connected == false)
                {
                    button2.Text = "Connect";
                    button2.BackColor = Color.LightGray;
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //button to write to the off the PLCs
            if (m_client.Connected == true)
            {
                if (m_client.WriteDeviceBlock("M30", 1, DataType.DataTypeString, textBox1.Text) != null)
                {
                    textBox1.Text = (string)m_client.WriteDeviceBlock("M30", 1, DataType.DataTypeString, textBox1.Text);
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //button to reading the data from the PLCs
            if (m_client.Connected == true)
            {
                if (m_client.ReadDeviceBlock("M30", 1, DataType.DataTypeString) != null)
                {
                    textBox1.Text = (string)m_client.ReadDeviceBlock("M30", 1, DataType.DataTypeString);
                }
            }
        }
    }
}