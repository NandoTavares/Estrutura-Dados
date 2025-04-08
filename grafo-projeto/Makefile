CXX = g++
CXXFLAGS = -Wall -std=c++17

SRC = main.cpp graph.cpp bfs.cpp dfs.cpp
OBJ = $(SRC:.cpp=.o)
EXEC = grafo

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CXX) $(OBJ) -o $(EXEC)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(EXEC)