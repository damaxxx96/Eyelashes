import axios from "axios";

export const TweezerService = {
  fetchTweezers: async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/tweezer/tweezerlist"
      );

      return response.data;
    } catch (error) {
      console.error("Error fetching tweezers:", error);
      return [];
    }
  },
};
