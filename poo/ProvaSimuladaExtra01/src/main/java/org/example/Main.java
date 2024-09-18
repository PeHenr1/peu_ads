package org.example;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.

public class Main {
    public static void main(String[] args) {
        // 1. Criação de dois usuários
        UserAccount user1 = new UserAccount("Alice","alice@gmail.com");
        UserAccount user2 = new UserAccount("Bob","bob.aissa@gmail.com");
        UserAccount user3 = new UserAccount("Charlie","char.lie@hotmail.com");

        // 2. Bob e Charlie segue Alice
        System.out.println("Bob e Charlie seguem Alice");
        user1.acceptFollower(user2);
        user1.acceptFollower(user3);

        // 3. Alice faz duas postagens
        System.out.println("\nAlice publica duas postagens:");
        user1.publish("Seja a mudança que você quer ver no mundo.");
        user1.publish("Acredite em você mesmo e tudo será possível.");

        // 4. Bob visualiza a timeline e interage com as postagens
        System.out.println("\nTimeline de Bob após Alice publicar duas mensagens:");
        System.out.println(user2.showTimeLine());

        System.out.println("\nBob aplaude a primeira postagem e vaia a segunda:");
        user2.clapPost(0); // Aplaude o primeiro post
        user2.booPost(1);  // Vai o segundo post
        System.out.println(user2.showTimeLine()); // Exibe timeline atualizada com claps e boos

        // 5. Alice bloqueia Charlie, que tenta segui-la
        System.out.println("\nCharlie tenta seguir Alice, mas é bloqueado:");
        user1.acceptFollower(user3);
        user1.blockAccount(user3);
         // Tenta seguir, mas foi bloqueado (não será adicionado à lista)

        // 6. Alice faz outra postagem (Charlie não deve vê-la)
        System.out.println("\nAlice publica uma nova postagem (Charlie não deve ver):");
        user1.publish("Nunca desista dos seus sonhos.");
        System.out.println("\nTimeline de Bob (deve incluir a nova postagem):");
        System.out.println(user2.showTimeLine());

        System.out.println("\nTimeline de Charlie (deve estar vazia pois ele foi bloqueado):");
        System.out.println(user3.showTimeLine()); // Charlie não segue Alice, então timeline vazia

        // 7. Alice remove a primeira postagem
        System.out.println("\nAlice remove a primeira postagem:");
        user1.delete(0); // Remove o primeiro post
        System.out.println("\nAlice publica uma nova mensagem:");
        user1.publish("A persistência é o caminho do êxito.");
        System.out.println("\nTimeline de Alice:");
        System.out.println(user1.showTimeLine());

        // 8. Testando limites da timeline
        System.out.println("\nTestando limite da timeline (10 posts)");
        for (int i = 0; i < 10; i++) {
            user1.publish("Post extra número " + (i + 1));
        }
        System.out.println("\nTimeline de Alice após 10 novas postagens:");
        System.out.println(user1.showTimeLine()); // Deve mostrar apenas as últimas 10 postagens

        // 9. Exibe as postagens de Alice
        System.out.println("\nExibindo todas as postagens de Alice:");
        System.out.println(user1.showMyPosts());

        // 10. Exibe os seguidores de Alice
        System.out.println("\nExibindo os seguidores de Alice:");
        System.out.println(user1.showMyFriends());
    }
}

