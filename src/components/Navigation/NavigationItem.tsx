import React from 'react';

export interface NavigationItemProps {
  href: string;
  label: string;
  isActive?: boolean;
  onClick?: () => void;
}

/**
 * Individual navigation link component with accessibility features
 * Handles keyboard navigation and ARIA attributes
 */
export const NavigationItem: React.FC<NavigationItemProps> = ({
  href,
  label,
  isActive = false,
  onClick,
}) => {
  const handleKeyDown = (event: React.KeyboardEvent<HTMLAnchorElement>) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      onClick?.();
    }
  };

  return (
    <a
      href={href}
      className={`navigation-item ${isActive ? 'active' : ''}`}
      onClick={onClick}
      onKeyDown={handleKeyDown}
      aria-current={isActive ? 'page' : undefined}
      role="menuitem"
    >
      {label}
    </a>
  );
};
