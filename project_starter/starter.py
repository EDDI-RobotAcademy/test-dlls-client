import os
import sys

import colorama

from user_defined_protocol.register import UserDefinedProtocolRegister

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))

from template.client_socket.service.client_socket_service_impl import ClientSocketServiceImpl
from template.command_analyzer.service.command_analyzer_service_impl import CommandAnalyzerServiceImpl
from template.command_executor.service.command_executor_service_impl import CommandExecutorServiceImpl
from template.initializer.init_domain import DomainInitializer
from template.os_detector.detect import OperatingSystemDetector
from template.os_detector.operating_system import OperatingSystem
from template.receiver.service.receiver_service_impl import ReceiverServiceImpl
from template.thread_worker.service.thread_worker_service_impl import ThreadWorkerServiceImpl
from template.transmitter.service.transmitter_service_impl import TransmitterServiceImpl
from template.utility.color_print import ColorPrinter
from template.request_generator.request_class_map import RequestClassMap
from template.response_generator.response_class_map import ResponseClassMap

DomainInitializer.initEachDomain()
UserDefinedProtocolRegister.registerUserDefinedProtocol()


if __name__ == "__main__":
    colorama.init(autoreset=True)

    responseClassMapInstance = ResponseClassMap.getInstance()
    requestClassMapInstance = RequestClassMap.getInstance()
    requestClassMapInstance.printRequestClassMap()

    detectedOperatingSystem = OperatingSystemDetector.checkCurrentOperatingSystem()
    ColorPrinter.print_important_data("detectedOperatingSystem", detectedOperatingSystem)

    if detectedOperatingSystem is OperatingSystem.UNKNOWN:
        ColorPrinter.print_important_message("범용 운영체제 외에는 실행 할 수 없습니다!")
        exit(1)

    clientSocketService = ClientSocketServiceImpl.getInstance()
    clientSocket = clientSocketService.createClientSocket()
    clientSocketService.connectToTargetHostUnitSuccess()

    transmitterService = TransmitterServiceImpl.getInstance()
    transmitterService.requestToInjectUserDefinedResponseClassMapInstance(responseClassMapInstance)

    receiverService = ReceiverServiceImpl.getInstance()
    receiverService.requestToInjectUserDefinedRequestClassMapInstance(requestClassMapInstance)

    commandAnalyzerService = CommandAnalyzerServiceImpl.getInstance()
    commandExecutorService = CommandExecutorServiceImpl.getInstance()

    threadWorkerService = ThreadWorkerServiceImpl.getInstance()
    threadWorkerService.createThreadWorker("Receiver", receiverService.requestToReceiveCommand)
    threadWorkerService.executeThreadWorker("Receiver")

    threadWorkerService.createThreadWorker("CommandAnalyzer", commandAnalyzerService.analysisCommand)
    threadWorkerService.executeThreadWorker("CommandAnalyzer")

    threadWorkerService.createThreadWorker("CommandExecutor", commandExecutorService.executeCommand)
    threadWorkerService.executeThreadWorker("CommandExecutor")

    threadWorkerService.createThreadWorker("Transmitter", transmitterService.requestToTransmitResult)
    threadWorkerService.executeThreadWorker("Transmitter")
