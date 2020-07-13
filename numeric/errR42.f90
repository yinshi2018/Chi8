((-(chi4(num1,num2)/chi2(num1,num2)**2))**2*errc2(num2)**2 + 
    (1/chi2(num1,num2) - chi4(num1,num2)/chi2(num1,num2)**2*0.5*
         ((4*num1)/T(num2))**2)**2*errc4(num2)**2 + 
    ((0.5*((4*num1)/T(num2))**2)/chi2(num1,num2) - 
        chi4(num1,num2)/chi2(num1,num2)**2*1/(4.*3.*2.)*
         ((4*num1)/T(num2))**4)**2*errc6(num2)**2 + 
    ((1/(4.*3.*2.)*((4*num1)/T(num2))**4)/chi2(num1,num2) - 
        chi4(num1,num2)/chi2(num1,num2)**2*1/(6.*5.*4.*3.*2.)*
         ((4*num1)/T(num2))**6)**2*errc8(num2)**2)**0.5
