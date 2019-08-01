safe([V2,V1,_]) :-
(V1 =< V2 ; V2 = 0),
C is 3-V1, D is 3-V2,
(C =< D; D = 0).


find :-
path([3,3,left],[0,0,right],[[3,3,left]],_).
printText([]) :- nl, nl.
printText([[A,B,String]|T]) :-
printText(T),
write('Current left side: '), write(B), write(' New left side: '), write(A), write(': '), write(String), nl.

path([A,B,C],[A,B,C],_,MoveList):-
nl,nl,printText(MoveList).

path([A,B,C],[D,E,F],Traversed,Moves) :-
move([A,B,C],[I,J,K],Out),
safe([I,J,K]), % Checks for safe move
not(member([I,J,K],Traversed)), 
path([I,J,K],[D,E,F],[[I,J,K]|Traversed],[ [[I,J,K],[A,B,C],Out] | Moves ]).

move([A,B,left],[C,B,right],'One missionary                  ->') :-
A > 0, C is A - 1.
move([A,B,left],[C,B,right],'Two missionaries                ->') :-
A > 1, C is A - 2.
move([A,B,left],[C,D,right],'One missionary and One cannibal ->') :-
A > 0, B > 0, C is A - 1, D is B - 1.
move([A,B,left],[A,D,right],'One cannibal                    ->') :-
B > 0, D is B - 1.
move([A,B,left],[A,D,right],'Two cannibals                   ->') :-
B > 1, D is B - 2.
move([A,B,right],[C,B,left],'One missionary                  <-') :-
A < 3, C is A + 1.
move([A,B,right],[C,B,left],'Two missionaries                <-') :-
A < 2, C is A + 2.
move([A,B,right],[C,D,left],'One missionary and One cannibal <-') :-
A < 3, B < 3, C is A + 1, D is B + 1.
move([A,B,right],[A,D,left],'One cannibal returns            <-') :-
B < 3, D is B + 1.
move([A,B,right],[A,D,left],'Two cannibals return            <-') :-
B < 2, D is B + 2.