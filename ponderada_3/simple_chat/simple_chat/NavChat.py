def main():
    print('Hi from simple_chat.')


if __name__ == '__main__':
    main()
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import re
    
class UserRequisitionManager:
    def __init__(self, intentions, actions):
        self.intentions = intentions
        self.actions = actions

    def manage_requisition(self, requisition):
        requisition = requisition.lower().strip()

        for intention, patterns in self.intentions.items():
            for pattern in patterns:
                match = re.match(pattern, requisition, re.IGNORECASE)
                if match:
                    response = self.actions[intention](match.group(1))
                    return response
                
        return "Me desculpe. Não entendi o comando. Você poderia repetir, por gentileza?"
    
class NavChat(Node):
    def __init__(self, user_requisition):
        super().__init__('navchat')
        self.requisition = user_requisition
        self.publisher_ = self.create_publisher(String, 'navchat', 10)
        self.subscription = self.create_subscription(
            String,
            'navchat',
            self.listener_callback,
            10)
        self.subscription
        self.get_logger().info("O chatbot de navegação foi iniciado com sucesso")

    def listener_callback(self, msg):
        self.get_logger().info('Requisição do usuário: "%s"' % msg.data)
        response = self.requisition.manage_requisition(msg.data)
        self.get_logger().info('Resposta: "%s"' % response)
        response_msg = String()
        response_msg.data = response
        self.publisher_.publish(response_msg)

    def main(args=None):

        rclpy.init(args=args)

        intentions = {
            "go_to": [
                r"Quero ser levado (?:para|ao|à|a|aos|às)? (.+)",
                r"Ir para (?:o|a|os|as)? (.+)",
                r"Encaminhe-me (?:para|ao|à|aos|a|às)? (.+)",
                r"Leve-me at[eé] (?:o|a|os|as)? (.+)",
                r"Preciso ir (?:para|ao|à|aos|às|a)? (.+)",
                r"Dirija-se (?:ao|à|aos|às)? (.+)",
                r"Partir (?:para|ao|à|aos|às)? (.+)",
                r"Mudar-se para (?:o|a|os|as)? (.+)",
                r"Tomar o caminho (?:para|ao|à|a|aos|às)? (.+)",
                r"Quero navegar (?:para|ao|à|aos|às)? (.+)",
                r"V[áa] para (?:o|a|os|as)? (.+)",
                r"Quero ir (?:para|ao|à|aos|às|a)? (.+)",
                r"Me leve (?:a|à)? (.+)",
                r"V[áa] para (.+)",
                r"Desloque-se (?:para|ao|à|aos|às)? (.+)",
                r"Rumo (?:a|ao|à|aos|às)? (.+)",
                r"Por favor, me encaminhe (?:para|ao|à|a|aos|às)? (.+)",
                r"Leve-me at[eé] (?:o|a|os|as)? (.+)",
                r"Pode me levar (?:para|ao|à|a|aos|às)? (.+)",
                r"Encaminhe-me (?:para|ao|à|aos|a|às)? (.+)"

            ],
        }

        actions = {
            "go_to": lambda place: "Comando compreendido, indo para " + place,
        }

        user_query = input("Olá, eu sou o chatbot de navegação. Como posso ajudar? ")
        
        processed_user_query = UserRequisitionManager(intentions, actions)
        navchat_answer = processed_user_query.manage_requisition(user_query)

        print(navchat_answer)

    if __name__ == "__main__":
        main()