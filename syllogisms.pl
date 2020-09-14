wahrheitswert(u).
wahrheitswert(a).
wahrheitswert(n).

gf:-

write('Bitte geben Sie die Geltungswertformel 1 (Form: W.X.Y.Z.) ein:'),
  nl,
  read(W),read(X),read(Y),read(Z),
  wahrheitswert(W),wahrheitswert(X),wahrheitswert(Y),wahrheitswert(Z),
  write('Danke für die Eingabe:'),
  write(W),write(X),write(Y),write(Z),nl,
write('Bitte geben Sie die Geltungswertformel 2 (Form: A.B.C.D.) ein:'),
  nl,
  read(A),read(B),read(C),read(D),
  wahrheitswert(A),wahrheitswert(B),wahrheitswert(C),wahrheitswert(D),
  write('Danke für die Eingabe:'),
  write(A),write(B),write(C),write(D),nl,
print_syl_schließen(W,X,Y,Z,A,B,C,D).

print_syl_schließen(W,X,Y,Z,A,B,C,D):-
	nl,nl,nl,
	write('--------------------------------------------'),nl,
	write('Prämisse1:  '),
  write(W),write('-'),write(W),tab(1),write(X),write('-'),write(X),tab(1),
  write(Y),write('-'),write(Y),tab(1),write(Z),write('-'),write(Z),tab(1),nl,
	write('Prämisse2:  '),
  write(A),tab(1),write(B),tab(1),write(C),tab(1),write(D),write(','),
  write(A),tab(1),write(B),tab(1),write(C),tab(1),write(D),tab(1),nl,
	write('--------------------------------------------'),nl,
	gf(W,W,X,X,Y,Y,Z,Z,A,B,C,D,A,B,C,D,M,N,O,P).
	

	gf(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D):-
				(W_1==n,X_1==n,A=n,gf2(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(A_1==n,X_1==n,A=n,gf2(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(W_1==n,C_1==n,A=n,gf2(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(A_1==n,C_1==n,A=n,gf2(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));				
				(W_1==a,B_1==n,A_1\==n,A=a,gf2(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(A_1==a,Y_1==n,W_1\==n,A=a,gf2(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(X_1==a,D_1==n,C_1\==n,A=a,gf2(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(C_1==a,Z_1==n,X_1\==n,A=a,gf2(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
	   (		(W_1\==n;X_1\==n),
				(A_1\==n;X_1\==n),
				(W_1\==n;C_1\==n),
				(A_1\==n;C_1\==n),			
				(W_1\==a;B_1\==n;A_1==n),
				(A_1\==a;Y_1\==n;W_1==n),
				(X_1\==a;D_1\==n;C_1==n),
				(C_1\==a;Z_1\==n;X_1==n),A=u,!,gf2(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D)).

gf2(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D):-
				(W_2==n,X_2==n,B=n,gf3(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(B_1==n,X_2==n,B=n,gf3(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(W_2==n,D_1==n,B=n,gf3(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(B_1==n,D_1==n,B=n,gf3(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(W_2==a,A_1==n,B_1\==n,B=a,gf3(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(B_1==a,Y_2==n,W_2\==n,B=a,gf3(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(X_2==a,C_1==n,D_1\==n,B=a,gf3(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(D_1==a,Z_2==n,X_2\==n,B=a,gf3(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
		(		(W_2\==n;X_2\==n),
				(B_1\==n;X_2\==n),
				(W_2\==n;D_1\==n),
				(B_1\==n;D_1\==n),
				(W_2\==a;A_1\==n;B_1==n),
				(B_1\==a;Y_2\==n;W_2==n),
				(X_2\==a;C_1\==n;D_1==n),
				(D_1\==a;Z_2\==n;X_2==n),B=u,!,gf3(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D)).	   
gf3(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D):- 
				(Y_1==n,Z_1==n,C=n,gf4(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(A_2==n,Z_1==n,C=n,gf4(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(Y_1==n,C_2==n,C=n,gf4(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(A_2==n,C_2==n,C=n,gf4(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(Y_1==a,B_2==n,A_2\==n,C=a,gf4(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(A_2==a,W_1==n,Y_1\==n,C=a,gf4(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(Z_1==a,D_2==n,C_2\==n,C=a,gf4(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(C_2==a,X_1==n,Z_1\==n,C=a,gf4(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
			(	(Y_1\==n;Z_1\==n),
				(A_2\==n;Z_1\==n),
				(Y_1\==n;C_2\==n),
				(A_2\==n;C_2\==n),
				(Y_1\==a;B_2\==n;A_2==n),
				(A_2\==a;W_1\==n;Y_1==n),
				(Z_1\==a;D_2\==n;C_2==n),
				(C_2\==a;X_1\==n;Z_1==n),C=u,!,gf4(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D)).
gf4(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D):-
				(Y_2==n,Z_2==n,D=n,gf5(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(B_2==n,Z_2==n,D=n,gf5(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(Y_2==n,D_2==n,D=n,gf5(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(B_2==n,D_2==n,D=n,gf5(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(Y_2==a,A_2==n,B_2\==n,D=a,gf5(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(B_2==a,W_2==n,Y_2\==n,D=a,gf5(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(Z_2==a,C_2==n,D_2\==n,D=a,gf5(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
				(D_2==a,X_2==n,Z_2\==n,D=a,gf5(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D));
			(	(Y_2\==n;Z_2\==n),
				(B_2\==n;Z_2\==n),
				(Y_2\==n;D_2\==n),
				(B_2\==n;D_2\==n),
				(Y_2\==a;A_2\==n;B_2==n),
				(B_2\==a;W_2\==n;Y_2==n),
				(Z_2\==a;C_2\==n;D_2==n),
				(D_2\==a;X_2\==n;Z_2==n),D=u,!,gf5(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D)).

gf5(W_1,W_2,X_1,X_2,Y_1,Y_2,Z_1,Z_2,
	   A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2,A,B,C,D)	:- 	write('Konklusion: '),
				write(A),tab(1),write(B),tab(1),write(A),tab(1),write(B),tab(1),
				write(C),tab(1),write(D),tab(1),write(C),tab(1),write(D),nl,nl,
				
													A==a,B==u,C==n,D==a,write('Alle S sind P');
													A==a,B==u,C==u,D==u,write('Einige S sind P');
													A==n,B==a,C==a,D==u,write('Kein S ist P');
													A==u,B==u,C==a,D==u,write('Einige S sind keine P').
	