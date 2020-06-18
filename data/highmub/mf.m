clear
for i=0:1:40
    chi2=load(strcat('mub',num2str(10*i),'/final/buffer/chi2.dat'));
    chi4=load(strcat('mub',num2str(10*i),'/final/buffer/chi4.dat'));
    chi6=load(strcat('mub',num2str(10*i),'/final/buffer/chi6.dat'));
    chi8=load(strcat('mub',num2str(10*i),'/final/buffer/chi8.dat'));
    R42(:,i+1)=chi4./chi2;
    R62(:,i+1)=chi6./chi2;
    R82(:,i+1)=chi8./chi2;
end


