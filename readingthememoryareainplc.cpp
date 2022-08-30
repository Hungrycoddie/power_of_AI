		/// </summary>
		/// <param name="table"></param>
		/// <param name="tableIndex"></param>
		/// <param name="area"></param>
		/// <param name="areaIndex"></param>
		/// <returns></returns>
		public string[] ReadAll(string table, int tableIndex, string area, int areaIndex)
		{
			if (string.IsNullOrEmpty(table))
			{
				return null;
			}
			//get the memory area in plc's address table, and return a string array of the data
			return ReadAll(table, tableIndex, new string[] { area }, areaIndex);
		}

		/// <summary>
		/// read the memory area in plc's address table, and return a string array of the data
		/// </summary>
		/// <param name="table"></param>
		/// <param name="tableIndex"></param>
		/// <param name="area"></param>
		/// <param name="areaIndex"></param>
		/// <param name="start"></param>
		/// <param name="count"></param>
		/// <returns></returns>
		public string[] ReadAll(string table, int tableIndex, string area, int areaIndex, int start, int count)
		{
			if (string.IsNullOrEmpty(table))
			{
				return null;
			}
			//get the memory area in plc's address table, and return a string array of the data
			return ReadAll(table, tableIndex, new string[] { area }, areaIndex, start, count);
		}

		/// <summary>
		/// read the memory areas in plc's address table, and return a string array of the data
		/// </summary>
		/// <param name="table"></param>
		/// <param name="tableIndex"></param>
		/// <param name="areas"></param>
		/// <param name="areaIndex"></param>
		/// <returns></returns>
		public string[] ReadAll(string table, int tableIndex, string[] areas, int areaIndex)
		{
			if (string.IsNullOrEmpty(table))
			{
				return null;
			}
			//get the memory area in plc's address table, and return a string array of the data
			return ReadAll(table, tableIndex, areas, areaIndex, 0, -1);
		}

		/// <summary>
		/// read the memory areas in plc's address table, and return a string array of the data
		/// </summary>
		/// <param name="table"></param>
		/// <param name="tableIndex"></param>
		/// <param name="areas"></param>
		/// <param name="areaIndex"></param>
		/// <param name="start"></param>
		/// <param name="count"></param>
		/// <returns></returns>
		public string[] ReadAll(string table, int tableIndex, string[] areas, int areaIndex, int start, int count)
		{
			if (string.IsNullOrEmpty(table))
			{
				return null;
			}
			//get the memory area in plc's address table, and return a string array of the data
			if (areas == null || areas.Length == 0)
			{
				return null;
			}
			if (tableIndex < 0)
			{
				tableIndex = 0;
			}
			if (areaIndex < 0)
			{
				areaIndex = 0;
			}
			if (count <= 0)
			{
				count = -1;
			}
			List<string> lst = new List<string>();
			for (int a = 0; a < areas.Length; a++)
			{
				string[] vals = ReadAll(table, tableIndex, areas[a], areaIndex, start, count);
				if (vals != null && vals.Length > 0)
				{
					lst.AddRange(vals);
				}
			}
			if (lst.Count > 0)
			{
				return lst.ToArray();
			}
			return null;
		}
		/// <summary>
		/// read the memory area in plc's address table, and return a string array of the data
		/// </summary>
		/// <param name="table"></param>
		/// <param name="tableIndex"></param>
		/// <param name="area"></param>
		/// <param name="areaIndex"></param>
		/// <returns></returns>
		public string[] ReadAll(string table, string area, int areaIndex)
		{
			if (string.IsNullOrEmpty(table))
			{
				return null;
			}
			//get the memory area in plc's address table, and return a string array of the data
			return ReadAll(table, 0, new string[] { area }, areaIndex);
		}

		/// <summary>
		/// read the memory area in plc's address table, and return a string array of the data
		/// </summary>
		/// <param name="table"></param>
		/// <param name="tableIndex"></param>
		/// <param name="area"></param>
		/// <param name="areaIndex"></param>
		/// <param name="start"></param>
		/// <param name="count"></param>
		/// <returns></returns>
		public string[] ReadAll(string table, string area, int areaIndex, int start, int count)
		{
			if (string.IsNullOrEmpty(table))
			{
				return null;
			}
			//get the memory area in plc's address table, and return a string array of the data
			return ReadAll(table, 0, new string[] { area }, areaIndex, start, count);
		}

		/// <summary>
		/// read the memory areas in plc's address table, and return a string array of the data
		/// </summary>
		/// <param name="table"></param>
		/// <param name="tableIndex"></param>
		/// <param name="areas"></param>
		/// <param name="areaIndex"></param>
		/// <returns></returns>
		public string[] ReadAll(string table, string[] areas, int areaIndex)
		{
			if (string.IsNullOrEmpty(table))
			{
				return null;
			}
			//get the memory area in plc's address table, and return a string array of the data
			return ReadAll(table, 0, areas, areaIndex, 0, -1);
		}

		/// <summary>
		/// read the memory areas in plc's address table, and return a string array of the data
		/// </summary>
		/// <param name="table"></param>
		/// <param name="tableIndex"></param>
		/// <param name="areas"></param>
		/// <param name="areaIndex"></param>
		/// <param name="start"></param>
		/// <param name="count"></param>
		/// <returns></returns>
		public string[] ReadAll(string table, string[] areas, int areaIndex, int start, int count)
		{
			if (string.IsNullOrEmpty(table))
			{
				return null;
			}
			//get the memory area in plc's address table, and return a string array of the data
			return ReadAll(table, 0, areas, areaIndex, start, count);
		}
		