CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra -O3 -DNDEBUG
LDFLAGS = -static -static-libgcc -static-libstdc++

SRCS = Solver.cpp
OBJS = $(SRCS:.cpp=.o)

all: c4solver generator

c4solver: $(OBJS) main.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o c4solver.exe main.o $(OBJS)

generator: generator.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o generator.exe generator.o

clean:
	rm -f *.o c4solver.exe generator.exe