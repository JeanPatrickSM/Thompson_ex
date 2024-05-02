def dominio_emails(emails):
  
  conta_dominios = {}

  for email in emails:
   
    dominio = email.split("@")[1]

    if dominio in conta_dominios:
      
      conta_dominios[dominio] += 1
    else:
     
      conta_dominios[dominio] = 1

  ordena_dominio = sorted(conta_dominios.items(), key=lambda item: item[1], reverse=True)

  return ordena_dominio

emails = ["jeanpatrick115@hotmail.com", "vinao@hotmail.com", "hugoh@hotmail.com",
          "Rafa@yahoo.com", "diegor@gmail.com", "anaclara@gmail.com"]

mais_popular = dominio_emails(emails)

print(mais_popular)
