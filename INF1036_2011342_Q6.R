


farmacia<- function(n,tmax){
  contaAtendimento <- 0
  contaNãoAtendimiento <- 0
  for (i in 1:n){
    Att = rep(0,5)
    t = 0
    while(t<tmax){
      TC = rexp(1,1/2)
      t = t + TC
      for (iA in 1:length(Att)){
        if(Att[iA]>TC){
          Att[iA] = Att[iA] - TC
        }
        else{
          Att[iA] = 0
        }
      }
      iAttendente = GetAttendente(Att)
      if (iAttendente!=0){
        contaAtendimento = contaAtendimento + 1
        TA = rexp(1,1/4)
        Att[iAttendente] = TA
      }
      else{
        contaNãoAtendimiento = contaNãoAtendimiento + 1
      }
    }
  }
  res = c(contaAtendimento,contaNãoAtendimiento)
  return(res)
}
GetAttendente<-function(Attendentes){
  for(i in 1:length(Attendentes)){
    if (Attendentes[i] == 0){
      return (i)
    }
    else{
      return (0)
    }
  }
}
#Letra A)
resp = farmacia(1,36000)
print(paste("Atendimentos realizados: ",resp[1] ))
print(paste("Atendimentos não realizados: ",resp[2]))

#Letra B)
n = 50
resp = (farmacia(n,36000))/n
print(paste("Média de Atendimentos realizados: ",resp[1] ))
print(paste("Média Atendimentos não realizados: ",resp[2]))
