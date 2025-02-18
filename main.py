    def _check_proxy(self) -> None:
        """
        Проверяет, что прокси работает, сравнивая ip профиля и прокси, вызывает исключение, если не совпадают
        :return: None
        """
        ip, port, login, password = self.proxy.split(":")
        current_ip = self._get_ip()
        logger.error(f"{self.profile_number} Текущий ip: {current_ip}")
        if current_ip != ip:
            raise Exception("Прокси не работает")

    def _get_ip(self) -> str:
        """
        # Получает ip текущего профиля
        # :return: ip_check_browser_status
        # """
        try:
            ip = self.page.evaluate('''
                        async () => {
                            const response = await fetch('https://api.ipify.org');
                            const data = await response.text();
                            return data;
                        }
